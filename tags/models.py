"""
Tags Models
"""
from typing import Dict

from database.core import db
from products.models import products_tags
import uuid


class Tags(db.Model):
    """
    Model of Tags
    """
    __tablename__ = 'Tags'
    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(50), default=uuid.uuid4().__str__(), unique=True)
    name = db.Column(db.String(50), unique=True)
    products = db.relationship('Products', secondary=products_tags, back_populates='tags')

    def set_uuid(self, uuid_):
        """
        Set uuid
        :param uuid_: uuid value
        """
        self.uuid = uuid_

    def serialize(self) -> Dict:
        """
        Serialize Model
        :return: Dict
        """
        return {
            'id': self.id,
            'uuid': self.uuid,
            'name': self.name,
            'products': [product.serialize() for product in self.products]
        }
