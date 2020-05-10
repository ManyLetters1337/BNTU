"""
Groups class
"""
from database.core import db
import uuid


class Groups(db.Model):
    """
    Model of Groups
    """
    __tablename__ = 'groups'
    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(50), default=uuid.uuid4().__str__(), unique=True)
    number = db.Column(db.String(50), unique=True)
    users = db.relationship('Users', backref='groups', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'number': self.number,
            'users': [user.serialize() for user in self.users]
        }

