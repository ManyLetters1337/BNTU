"""
Orders class
"""
from typing import Dict

from config import STATUSES
from database.core import db
from datetime import datetime
import uuid

orders_products = db.Table('orders_products',
                           db.Column('order_id', db.Integer, db.ForeignKey('orders.id')),
                           db.Column('product_id', db.Integer, db.ForeignKey('products.id'))
                           )


class Orders(db.Model):
    """
    Model of Orders
    """
    __tablename__ = 'orders'
    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(50), default=uuid.uuid4().__str__(), unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))
    address = db.Column(db.String(100))
    post_index = db.Column(db.String(50))
    status = db.Column(db.String(50), default='Active')
    created_date = db.Column(db.DateTime())
    products = db.relationship('Products', secondary=orders_products, back_populates='orders')

    def set_uuid(self, uuid_):
        """
        Set order uuid
        :param uuid_:
        """
        self.uuid = uuid_

    def accept(self):
        """
        Change Status to Accept
        :return:
        """
        self.status = STATUSES['Adopted']

    def set_user(self, user_):
        """
        Set user in products
        :param user_: User instance
        """
        self.user = user_

    def set_detail(self, **kwargs):
        """
        Set Order Detail
        :param kwargs:
        :return:
        """
        self.city = kwargs['city']
        self.country = kwargs['country']
        self.address = kwargs['address']           # need refactoring
        self.post_index = kwargs['post_index']

        self.status = 'Pending'

    def serialize(self) -> Dict:
        """
        Serialize Model
        :return: Dict
        """
        return {
            'id': self.id,
            'uuid': self.uuid,
            'user_id': self.user_id,
            'country': self.country,
            'city': self.city,
            'address': self.address,
            'post_index': self.post_index,
            'status': self.status,
            'created_date': self.created_date,
            'products': [product.serialize() for product in self.products],
            'user_name': self.user.first_name + ' ' + self.user.last_name,
            'user_uuid': self.user.uuid,
            'price': str(self.price)
        }

    @property
    def price(self):
        """
        Get Full Order Price
        :return:
        """
        total_price = 0
        for product in self.products:
            total_price += product.price

        return total_price
