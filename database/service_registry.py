"""
Initialize classes
"""
from categories.services import CategoriesDBServices
from comments.services import CommentsDBServices
from groups.services import GroupsDBServices
from orders.services import OrdersDBServices
from products.services import ProductsDBService
from tags.services import TagsDBService
from users.services import UsersDBService


class ServiceRegistry:

    def __init__(self):
        self.categories = CategoriesDBServices()
        self.comments = CommentsDBServices()
        self.groups = GroupsDBServices()
        self.orders = OrdersDBServices()
        self.products = ProductsDBService()
        self.tags = TagsDBService()
        self.users = UsersDBService()


services = ServiceRegistry()
