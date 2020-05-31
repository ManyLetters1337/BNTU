"""
User Class
"""
from typing import Dict

from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from database.core import db
from time import time
from config import secret_key
from products.models import products_users, rates_users
import jwt
import uuid


class Users(db.Model, UserMixin):
    """
    Model of User
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(50), default=uuid.uuid4().__str__(), unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(300))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    student_number = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    birthday_date = db.Column(db.Date(), nullable=True)
    about = db.Column(db.Text(), nullable=True)
    role = db.Column(db.String(50), default='user')
    orders = db.relationship('Orders', backref='user', lazy=True)
    comments = db.relationship('Comments', backref='user', lazy=True)
    products = db.relationship('Products', secondary=products_users, back_populates='users')
    rates = db.relationship('Rates', secondary=rates_users, back_populates='users')

    def set_uuid(self, uuid_: str):
        """
        Set user uuid
        :param uuid_:
        """
        self.uuid = uuid_

    def set_password(self, password: str):
        """
        Set user password_hash
        :param password:
        """
        self.password_hash = generate_password_hash(password)

    def get_reset_password_token(self, expire_in=600):
        """
        Get Reset Password Token for User
        @param expire_in:
        @return:
        """
        return jwt.encode({'reset_password': self.id, 'exp': time() + expire_in},
                          secret_key, algorithm='HS256').decode('utf-8')

    def serialize(self) -> Dict:
        """
        Serialize Model
        :return: Dict
        """
        return {
            'id': self.id,
            'uuid': self.uuid,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'group_id': self.group_id,
            'student_number': self.student_number,
            'birthday_date': self.birthday_date,
            'about': self.about,
            'role': self.role,
            'group': self.groups.number,
            'image': self.image,
            'orders': [order.serialize() for order in self.orders]
        }

