"""
Orders class
"""
from database.core import db
from datetime import datetime
import uuid


class Orders(db.Model):
    """
    Model of Orders
    """
    __tablename__ = 'Orders'
    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(50), default=uuid.uuid4().__str__(), unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))
    address = db.Column(db.String(100))
    post_index = db.Column(db.String(50))
    status = db.Column(db.String(50), default='Created')
    create_date = db.Column(db.DateTime(), default=datetime.now)
    products = db.relationship('Products', backref='orders', lazy=True)  # Change

    def set_uuid(self, uuid_):
        """
        Set order uuid
        :param uuid_:
        """
        self.uuid = uuid_

    def set_user(self, user_):
        """
        Set user in products
        :param user_: User instance
        """
        self.user = user_

    def serialize(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'user_id': self.user_id,
            'country': self.country,
            'city': self.city,
            'address': self.address,
            'post_index': self.post_index,
            'status': self.status,
            'create_date': self.create_date,
            'products': self.products.serialize()
        }
