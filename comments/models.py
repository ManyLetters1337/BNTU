"""
Comments class
"""
from typing import Dict

from database.core import db
from datetime import datetime
import uuid


class Comments(db.Model):
    """
    Model of Comments
    """
    __tablename__ = 'Comments'
    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(50), default=uuid.uuid4().__str__(), unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer(), db.ForeignKey('products.id'))
    text = db.Column(db.String(300), nullable=True)
    rate = db.Column(db.Integer(), default=0)
    create_date = db.Column(db.DateTime(), default=datetime.now())

    def set_uuid(self, uuid_):
        """
        Set uuid
        :param uuid_: uuid value
        """
        self.uuid = uuid_

    def set_user(self, user_):
        """
        Set user in comment
        :param user_: User instance
        """
        self.user = user_

    def set_product(self, product_):
        """
        Set product in comment
        :param product_: Product instance
        """
        self.product = product_

    def rate_up(self, value):
        """
        Up rate value
        :param value:
        """
        self.rate += value

    def rate_down(self, value):
        """
        Down rate value
        :param value:
        """
        self.rate -= value

    def serialize(self) -> Dict:
        """
        Serialize Model
        :return: Dict
        """
        return {
            'id': self.id,
            'uuid': self.uuid,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'text': self.text,
            'rate': self.rate,
            'create_date': self.create_date
        }
