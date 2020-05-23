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

    def create(self, user: 'Users') -> Orders:
        """
        Create Order Instance
        @return: Order Instance
        """
        order: 'Orders' = super().new(user_id=user.id)
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
        return db.session.query(self.model).filter(self.model.user == user).all()

    def get_active_order(self, user: 'User') -> 'Orders':
        """
        Get order with Active status for current USer
        :param user: User Instance
        :return:
        """
        order = db.session.query(self.model).filter(self.model.user == user).filter_by(status='Active').first()

        return order

    def product_is_added(self, order: 'Orders', product: 'Products') -> 'BOOL':
        """
        Check Product In Order
        :param order: Order Instance
        :param product: Product Instance
        :return: True or False
        """
        return product in order.products

    def remove_product(self, order: 'Orders', product: 'Products') -> 'Orders':
        """
        Remove Product from Order
        :param order: Order Instance
        :param product: Product Instance
        :return:
        """
        order.products.remove(product)

        self.commit()

        return order

    def set_order_detail(self, order: 'Orders', **kwargs) -> 'Orders':
        """
        Set Order Detail
        :param order:
        :param kwargs:
        :return: Order Instance
        """
        order.set_detail(**kwargs)

        self.commit()

        return order
