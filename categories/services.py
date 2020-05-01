"""
Database interaction methods for a Categories class
"""
import uuid

from database.base_services import BaseDBServices
from .models import Categories


class CategoriesDBServices(BaseDBServices):

    model = Categories

    def create(self, name: str) -> Categories:
        """
        Create Category Instance
        @return: Category Instance
        """
        category: Categories = super().new(name=name)
        category.set_uuid(uuid.uuid1().__str__())

        self.commit()

        return category
