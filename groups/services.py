"""
Database interaction methods for a Groups class
"""
import uuid

from database.base_services import BaseDBServices
from .models import Groups


class GroupsDBServices(BaseDBServices):

    model = Groups

    def create(self, number: str) -> Groups:
        """
        Create Group Instance
        @return: Group Instance
        """
        group: Groups = super().new(number=number)
        group.set_uuid(uuid.uuid1().__str__())

        self.commit()

        return group