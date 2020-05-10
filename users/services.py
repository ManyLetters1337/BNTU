"""
Database interaction methods for a User class
"""
from database.base_services import BaseDBServices
from .models import Users
from typing import TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    from products.models import Products
    from groups.models import Groups


class UsersDBService(BaseDBServices):
    model = Users

    def create(self, group: 'Groups', **kwargs) -> 'Users':
        """
        Create User Instance
        :param group: Group Instance
        :return:
        """
        user: 'Users' = super().new(group_id=group.id, email=kwargs['email'], first_name=kwargs['first_name'],
                                    last_name=kwargs['last_name'], student_number=kwargs['student_number'],
                                    birthday_date=kwargs['birthday_date'])
        user.set_password(kwargs['password'])
        user.set_uuid(uuid.uuid1().__str__())

        self.commit()

        return user
