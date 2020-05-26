"""
Database interaction methods for a Categories class
"""
import uuid
from typing import Dict, List

from database.base_services import BaseDBServices
from database.core import db
from products.models import Products
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

    def get_categories_statistic(self, category_statistic) -> 'Dict':
        """
        Get Categories With Products Count
        :return:
        """
        result = {}

        for category, products_buy_count in category_statistic.items():
            products_count: int = len(db.session.query(Products).filter_by(categories=category).all())

            result[category] = [products_count, products_buy_count]

        return result
