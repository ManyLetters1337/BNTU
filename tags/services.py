"""
Database interaction methods for a Tags class
"""
from database.base_services import BaseDBServices
from database.core import db
from typing import TYPE_CHECKING
from .models import Tags
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

    def get_tags_for_product(self, product: 'Products') -> 'List':
        """
        Get Tag List for Specific Product
        :param product: Specific Product
        :return:
        """
        return db.session.query(self.model).filter(self.model.products.any(id=product.id)).all()
