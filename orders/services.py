"""
Database interaction methods for a Orders class
"""
import uuid

from database.base_services import BaseDBServices
from database.core import db
from .models import Orders
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from users.models import Users
    from products.models import Products
    from typing import List


class OrdersDBServices(BaseDBServices):

    model = Orders

    def create(self, user: 'Users', product: 'Products', text: str) -> Orders:
        """
        Create Order Instance
        @return: Order Instance
        """
        order: 'Orders' = super().new(user_id=user.id, product_id=product.id, text=text)
        order.set_uuid(uuid.uuid1().__str__())

        self.commit()

        return order

    def add_product(self, order: 'Orders', product: 'Products') -> 'Orders':
        """
        Add product to Order
        :param order: Order Instance
        :param product: Product Instance
        :return:
        """
        order.products.append(product)

        self.commit()

        return order

    def delete_product(self, order: 'Orders', product: 'Products') -> 'Orders':
        """
        Delete product from Order
        :param order: Order Instance
        :param product: Product Instance
        :return:
        """
        order.products.remove(product)

        self.commit()

        return order

    def get_orders_for_product(self, product: 'Products') -> 'List':
        """
        Get Order List for Product
        :param product: Product Instance
        :return:
        """
        return db.session.query(self.model).filter(self.model.products.any(id=product.id)).all()

    def get_orders_for_user(self, user: 'Users') -> 'List':
        """
        Get Order List for User
        :param user: User Instance
        :return:
        """
        return db.session.query(self.model).filter(self.model.user.any(id=user.id)).all()
