"""
Database interaction methods for a Orders class
"""
import uuid

from database.base_services import BaseDBServices
from .models import Orders
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from users.models import User
    from products.models import Products


class OrdersDBServices(BaseDBServices):

    model = Orders

    def create(self, user: User, product: Products, text: str) -> Orders:
        """
        Create Order Instance
        @return: Order Instance
        """
        order: Orders = super().new(user_id=user.id, product_id=product.id, text=text)
        order.set_uuid(uuid.uuid1().__str__())

        self.commit()

        return order

    def add_product(self, order: Orders, product: Products) -> Orders:
        """
        Add product to Order
        :param order: Order Instance
        :param product: Product Instance
        :return:
        """
        order.products.append(product)

        self.commit()

        return order

    def delete_product(self, order: Orders, product: Products) -> Orders:
        """
        Delete product from Order
        :param order: Order Instance
        :param product: Product Instance
        :return:
        """
        order.products.remove(product)

        self.commit()

        return order
