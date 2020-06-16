"""
Database interaction methods for a User class
"""
from click import BOOL
import jwt
from flask import render_template
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.exceptions import NotFound

from config import secret_key
from database.base_services import BaseDBServices
from database.core import db
from typing import TYPE_CHECKING

from orders.models import Orders
from .models import Users
import uuid

if TYPE_CHECKING:
    from products.models import Products
    from groups.models import Groups
    from typing import List


class UsersDBService(BaseDBServices):
    model = Users

    def create(self, group: 'Groups', **kwargs) -> 'Users':
        """
        Create User Instance
        :param group: Group Instance
        :return:
        """
        user: 'Users' = super().new(group_id=group.id, email=kwargs['email'], first_name=kwargs['first_name'],
                                    last_name=kwargs['last_name'], student_number=kwargs['student_number'],
                                    image=kwargs['image']
                                    )
        user.set_password(kwargs['password'])
        user.set_uuid(uuid.uuid1().__str__())

        self.commit()

        return user

    def update_info(self, user: 'Users', image: str, about_info: str, birthday_date):
        """
        Update User Info
        :return:
        """
        if image:
            user.set_image(image)
        if about_info:
            user.set_about_info(about_info)
        if birthday_date:
            user.set_birthday_date(birthday_date)

        self.commit()

    def verify_reset_password_token(self, token):
        """
        Verify reset password token and return user Instance
        @param token: Reset Password Token
        @return: User Instance
        """
        try:
            id_ = jwt.decode(token, secret_key, algorithms=['HS256'])['reset_password']
        except jwt.ExpiredSignature as e:
            raise jwt.ExpiredSignatureError()

        return self.get_by_id_or_none(id_)

    def reset_password(self, user: 'Users', password: str):
        """
        Change User Password
        @param user:
        @param password:
        @return:
        """
        user.set_password(password)

        self.commit()

        return user

    def get_by_email(self, email: str) -> 'Users':
        """
        Get User by Email
        :param email: User Email
        :return: User Instance
        """
        try:
            return self.filter(email=email).first()
        except NoResultFound as e:
            raise NotFound()

    def get_by_student_number(self, student_number: str) -> 'Users':
        """
        Get User by student number
        :param student_number: Student number (str)
        :return: User Instance
        """
        try:
            return self.filter(student_number=student_number).first()
        except NoResultFound as e:
            raise NotFound()

    def get_password_hash(self, uuid_: str) -> 'password_hash':
        """
        Get password_hash for user
        :param uuid_: User uuid
        :return: Password_hash
        """
        try:
            return self.filter(uuid=uuid_).first().password_hash
        except NoResultFound as e:
            raise NotFound()

    def get_uuid_by_student_number(self, student_number: str) -> Users.uuid:
        """
        Get User uuid by student number
        :param student_number:
        :return:
        """
        try:
            return self.filter(student_number=student_number).first().uuid
        except NoResultFound as e:
            raise NotFound()

    def get_users_for_product(self, product: 'Products') -> 'List':
        """
        Get Users List for Specific Product
        :param product:
        :return:
        """
        return db.session.query(self.model).filter(self.model.products.any(id=product.id)).all()

    def add_product_to_order(self, user: 'Users', product: 'Products', order: 'Orders') -> 'BOOL':
        """
        Add Product To Order
        :param user: User Instance
        :param product: Product Instance
        :param order: Order Instance
        :return:
        """
        if product in order.products:
            order.products.remove(product)
            is_added = False
        else:
            order.products.append(product)
            is_added = True

        self.commit()

        return is_added
