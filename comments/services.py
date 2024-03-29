"""
Database interaction methods for a Comments class
"""
import uuid

from database.base_services import BaseDBServices
from database.core import db
from .models import Comments
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from users.models import User, Users
    from products.models import Products


class CommentsDBServices(BaseDBServices):

    model = Comments

    def create(self, user: 'User', product: 'Products', text: str) -> Comments:
        """
        Create Comments Instance
        @return: Comments Instance
        """
        comment: Comments = super().new(user_id=user.id, product_id=product.id, text=text)
        comment.set_uuid(uuid.uuid1().__str__())

        self.commit()

        return comment

    def get_for_product(self, product: 'Products'):
        """
        Get Comments for Product
        :param product: Product Instance
        :return:
        """
        return db.session.query(self.model).filter_by(product_id=product.id).order_by(db.desc(self.model.create_date))

    def get_for_user(self, user: 'Users'):
        """
        Get Comments for User
        :param user:
        :return:
        """
        return db.session.query(self.model).filter_by(user_id=user.id).all()
