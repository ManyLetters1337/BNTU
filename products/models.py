"""
Products Class
"""
from typing import Dict

from database.core import db
from datetime import datetime
from orders.models import orders_products
import uuid

products_tags = db.Table('Products_Tags',
                         db.Column('product_id', db.Integer, db.ForeignKey('Products.id')),
                         db.Column('tag_id', db.Integer, db.ForeignKey('Tags.id')),
                         )


class Products(db.Model):
    """
    Model of Products
    """
    __tablename__ = 'Products'
    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(50), default=uuid.uuid4().__str__(), unique=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer(), db.ForeignKey('Categories.id'))
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    create_date = db.Column(db.DateTime(), default=datetime.now)
    update_date = db.Column(db.DateTime())
    users = db.relationship('Users', backref='products', lazy=True)
    orders = db.relationship('Orders', secondary=orders_products, back_populates='products')
    tags = db.relationship('Tags', secondary=products_tags, back_populates='products')

    def set_uuid(self, uuid_):
        """
        Set products uuid
        :param uuid_:
        """
        self.uuid = uuid_

    def set_category(self, category):
        """
        Set category in products
        :param category:
        """
        self.category = category

    def serialize(self) -> Dict:
        """
        Serialize Model
        :return: Dict
        """
        return {
            'id': self.id,
            'uuid': self.uuid,
            'category_id': self.category_id,
            'price': self.price,
            'description': self.description,
            'create_date': self.create_date,
            'update_date': self.update_date,
            'category': self.category.serialize()
        }


class Rate(db.Model):
    """
    Model of Product Rate
    """
    __tablename__ = 'Rates'
    product_id = db.Column(db.Integer(), db.ForeignKey('Products.id'))
    rate = db.Column(db.Integer(), default=0)
    users = db.relationship('Users', backref='rate', lazy=True)

    def get_rate(self):
        """
        Get Rate for Product
        :return:
        """
        return self.rate / len(self.users)

    def up_rate(self, value):
        """
        Up rate
        :return:
        """
        self.rate += value
        return self.rate

    def check_user_rated(self, user):
        """
        Check if user already rate
        :param user: User instance
        :return:
        """
        if user in self.users:
            return True
        return False
