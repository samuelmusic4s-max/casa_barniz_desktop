from desktop.modules.inventory.core.errors.invalid_product_error import (
    InvalidProductError,
)
from desktop.modules.shared.entity import Entity

from desktop.modules.shared.value_objects.money import Money
from desktop.modules.shared.value_objects.non_empty_string import NonEmptyString


class Product(Entity):
    def __init__(
        self,
        id: NonEmptyString,
        name: NonEmptyString,
        description: NonEmptyString,
        category: list[NonEmptyString],
        list_price: Money,
    ):
        super().__init__(id)
        if not isinstance(name, NonEmptyString):
            raise InvalidProductError(
                "The parameter name must be a NonEmptyString object, not an ",
                name.__class__,
            )
        if not isinstance(description, NonEmptyString):
            raise InvalidProductError(
                "The parameter description must be a NonEmptyString object, not an ",
                description.__class__,
            )
        if not isinstance(category, list):
            raise InvalidProductError(
                "The parameter category must be a list[NonEmptyString], not an ",
                category.__class__,
            )
        for cat in category:
            if not isinstance(cat, NonEmptyString):
                raise InvalidProductError(
                    "The parameter category must be a list of NonEmptyString objects, not an ",
                    cat.__class__,
                )
        if not category:
            raise InvalidProductError("The parameter category must have at least one")
        if not isinstance(list_price, Money):
            raise InvalidProductError(
                "The parameter list_price must be an Money object, not an ",
                list_price.__class__,
            )
        self.name = name
        self.description = description
        self.category = category
        self.list_price = list_price

    def change_price(self, new_price: int):
        if new_price == 0:
            raise InvalidProductError(
                "The list_price of a product cannot be equals to zero"
            )
        self.list_price = Money(new_price)

    def change_name(self, new_name: str):
        self.name = NonEmptyString(new_name)

    def change_description(self, new_description: str):
        self.description = NonEmptyString(new_description)

    def add_category(self, new_category: str):
        self.category.append(NonEmptyString(new_category))

    def remove_category(self, category_id: int):
        if isinstance(category_id, bool) or not isinstance(category_id, int):
            raise InvalidProductError(
                "The parameter category_id must be an integer object"
            )
        if category_id < 0:
            raise InvalidProductError(
                "The parameter category_id must be greater or equals to zero"
            )
        if len(self.category) == 1:
            raise InvalidProductError("A product cannot be without a category")
        if category_id >= len(self.category):
            raise InvalidProductError("The parameter category_id is an invalid id")
        return self.category.pop(category_id)
