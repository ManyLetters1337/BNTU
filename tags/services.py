"""
Database interaction methods for a Tags class
"""
from database.base_services import BaseDBServices
from .models import Tags
from typing import TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    from products.models import Products


class TagsDBService(BaseDBServices):
    model = Tags

    def create(self, name: str) -> 'Tags':
        """
        Create Tag Instance
        :param name:
        :return:
        """
        tag: 'Tags' = super().new(name=name)
        tag.set_uuid(uuid.uuid1().__str__())

        self.commit()

        return tag

    def add_product(self, tag: 'Tags', product: 'Products') -> 'Tags':
        """
        Add Product To Tag
        :param tag: Tag Instance
        :param product: Product Instance
        :return: Tag Instance
        """
        tag.products.append(product)

        self.commit()

        return tag
