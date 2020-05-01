"""
Database interaction methods for a Comments class
"""
import uuid

from database.base_services import BaseDBServices
from .models import Comments
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from users.models import User
    from products.models import Products


class CommentsDBServices(BaseDBServices):

    model = Comments

    def create(self, user: User, product: Products, text: str) -> Comments:
        """
        Create Comments Instance
        @return: Comments Instance
        """
        comment: Comments = super().new(user_id=user.id, product_id=product.id, text=text)
        comment.set_uuid(uuid.uuid1().__str__())

        self.commit()

        return comment
