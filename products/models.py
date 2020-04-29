"""
Products Class
"""
from database.core import db
from datetime import datetime
import uuid


class Products(db.Model):
    """
    Model of Products
    """
    __tablename__ = 'Products'
    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(50), default=uuid.uuid4().__str__(), unique=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer(), db.ForeignKey('categories.id'))
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    create_date = db.Column(db.DateTime(), default=datetime.now)
    update_date = db.Column(db.DateTime())
    users = db.relationship('Users', backref='products', lazy=True)

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

    def serialize(self):
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
