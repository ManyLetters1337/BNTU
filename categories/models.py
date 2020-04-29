"""
Categories class
"""
from database.core import db
import uuid


class Categories(db.Model):
    """
    Model of Categories
    """
    _tablename_ = 'Categories'
    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(50), default=uuid.uuid4().__str__(), unique=True)
    name = db.Column(db.String(100), unique=True)
    products = db.relationship('Products', backref='categories', lazy=True)

    def set_uuid(self, uuid_):
        """
        Set uuid
        :param uuid_: uuid value
        """
        self.uuid = uuid_

    def serialize(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'name': self.name,
            'products': [product.serialize() for product in self.products]
        }
