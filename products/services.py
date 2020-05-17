"""
Database interaction methods for a Products class
"""
from database.base_services import BaseDBServices
from .models import Products
from typing import TYPE_CHECKING, List
import uuid

if TYPE_CHECKING:
    from categories.models import Categories
    from tags.models import Tags
    from orders.models import Orders


class ProductsDBService(BaseDBServices):
    model = Products

    def create(self, category: 'Categories', **kwargs) -> Products:
        """
        Create Product Instance
        @return: Product Instance
        """
        product: Products = super().new(category_id=category.id, name=kwargs['name'],
                                        price=kwargs['price'], description=kwargs['description'])
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

    def add_tags(self, product: 'Products', tags: List) -> Products:
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
