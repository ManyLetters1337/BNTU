"""
Database interaction methods for a Products class
"""
from database.base_services import BaseDBServices
from database.core import db
from typing import TYPE_CHECKING, Dict
from .models import Products
from categories.models import Categories
from orders.models import Orders
import uuid

if TYPE_CHECKING:
    from typing import List
    from users.models import Users
    from tags.models import Tags


class ProductsDBService(BaseDBServices):
    model = Products

    def create(self, category: 'Categories', **kwargs) -> Products:
        """
        Create Product Instance
        @return: Product Instance
        """
        product: Products = super().new(category_id=category.id, name=kwargs['name'],
                                        price=kwargs['price'], description=kwargs['description'], image=kwargs['image'])
        product.set_uuid(uuid.uuid1().__str__())

        product.set_update_time()

        self.commit()

        return product

    def update(self, product: 'Products', **kwargs) -> Products:
        """
        Update Product Instance
        :param product: Product instance
        :param kwargs:
        :return: Product Instance
        """
        if kwargs['price'] and product.price != kwargs['price']:
            product.price = kwargs['price']
        if kwargs['description'] and product.description != kwargs['description']:
            product.description = kwargs['description']
        if kwargs['category_id'] and product.category_id != kwargs['category_id']:
            product.category_id = kwargs['category_id']
        if kwargs['name'] and product.name != kwargs['name']:
            product.name = kwargs['name']

        self.commit()

        return product

    def add_tags(self, product: 'Products', tags: 'List') -> Products:
        """
        Add Tags to Product
        :param product: Product Instance
        :param tags: List of Tags
        :return:
        """
        for tag in tags:
            product.tags.append(tag)

        self.commit()

        return product

    def delete_tag(self, product: 'Products', tag: 'Tags') -> Products:
        """
        Delete Tag from Product
        :param product: Product Instance
        :param tag: Tag Instance
        :return:
        """
        product.tags.remove(tag)

        self.commit()

        return product

    def add_order(self, product: 'Products', order: 'Orders') -> Products:
        """
        Add Order To Product
        :param product: Product Instance
        :param order: Order Instance
        :return: Product Instance
        """
        product.orders.add(order)

        self.commit()

        return product

    def delete_order(self, product: 'Products', order: 'Orders') -> Products:
        """
        Delete Order from Product
        :param product: Product Instance
        :param order: Order Instance
        :return: Product Instance
        """
        product.orders.remove(order)

        self.commit()

        return product

    def get_product_with_category(self, category: 'Categories') -> 'List':
        """
        Get product list for specific Category
        :param category: Category Entity
        :return: List of Products
        """
        return db.session.query(self.model).filter_by(category_id=category.id).all()

    def get_product_for_user(self, user: 'Users') -> 'List':
        """
        Get Products List for specific User
        :param user: User Instance
        :return:
        """
        return db.session.query(self.model).filter(self.model.users.any(id=user.id)).all()

    def get_products_from_order(self, order: 'Orders'):
        """
        Get product from specific order
        :param order: Order Instance
        :return:
        """
        return db.session.query(self.model).filter(self.model.orders.any(id=order.id)).all()

    def get_products_buy_statistic(self):
        """
        Get Product Buyer Statistics
        :return:
        """
        orders: 'List' = db.session.query(Orders).filter_by(status='Paiding').all()
        products: 'List' = db.session.query(self.model).all()

        result = {}

        for product in products:
            numbers = 0
            for order in orders:
                if product in order.products:
                    numbers += 1
            result[product] = numbers

        return result

    def get_product_categories_statistic(self):
        """
        Get Product Categories Statistics
        :return:
        """
        product_buy_statistic: 'Dict' = self.get_products_buy_statistic()
        categories: 'List' = db.session.query(Categories).all()

        result = {}

        for category in categories:
            numbers = 0
            for product, value in product_buy_statistic.items():
                if product.categories == category:
                    numbers += value

            result[category] = numbers

        return result
