from desktop.modules.inventory.core.errors.invalid_lot_error import InvalidLotError
from desktop.modules.shared.entity import Entity
from desktop.modules.shared.value_objects.money import Money
from desktop.modules.shared.value_objects.non_empty_string import NonEmptyString
from desktop.modules.shared.value_objects.stock import Stock


class Lot(Entity):
    def __init__(
        self,
        id: NonEmptyString,
        product_id: NonEmptyString,
        support_id: NonEmptyString,
        buy_quantity: Stock,
        cost: Money,
        status: NonEmptyString,
        material: NonEmptyString,
        available_quantity: Stock,
        category: list[NonEmptyString],
    ) -> None:
        super().__init__(id)
        if not isinstance(product_id, NonEmptyString):
            raise InvalidLotError(
                "The parameter product_id must be a NonEmptyString object, not a ",
                product_id.__class__,
            )
        if not isinstance(support_id, NonEmptyString):
            raise InvalidLotError(
                "The parameter support_id must be a NonEmptyString object, not a ",
                support_id.__class__,
            )
        if not isinstance(buy_quantity, Stock):
            raise InvalidLotError(
                "The parameter buy_quantity must be a Stock object, not a ",
                buy_quantity.__class__,
            )
        if not isinstance(cost, Money):
            raise InvalidLotError(
                "The parameter cost must be a Money object, not a ", cost.__class__
            )
        if not isinstance(status, NonEmptyString):
            raise InvalidLotError(
                "The parameter status must be a NonEmptyString object, not a ",
                status.__class__,
            )
        if not isinstance(material, NonEmptyString):
            raise InvalidLotError(
                "The parameter material must be a NonEmptyString object, not a ",
                material.__class__,
            )
        if not isinstance(available_quantity, Stock):
            raise InvalidLotError(
                "The parameter available_quantity must be a Stock object, not a ",
                available_quantity.__class__,
            )
        if not isinstance(category, list):
            raise InvalidLotError(
                "The parameter category must be a list object, not a ",
                category.__class__,
            )
        for cat in category:
            if not isinstance(cat, NonEmptyString):
                raise InvalidLotError(
                    "The category must be a list of NonEmptyStrine object, not a list of ",
                    cat.__class__,
                    " objects",
                )
        self.product_id = product_id
        self.support_id = support_id
        self.buy_quantity = buy_quantity
        self.cost = cost
        self.status = status
        self.material = material
        self.available_quantity = available_quantity
        self.category = category

    def remove_quantity(self, quantity: int):
        r_quantity = Stock(quantity)
        self.available_quantity = self.available_quantity.remove_stock(r_quantity)

    def add_category(self, new_category: str):
        n_cat = NonEmptyString(new_category)
        self.category.append(n_cat)

    def remove_category(self, category_id: int):
        if isinstance(category_id, bool) or not isinstance(category_id, int):
            raise InvalidLotError("The parameter category_id must be an integer object")
        if category_id < 0:
            raise InvalidLotError(
                "The parameter category_id must be greater or equals to zero"
            )
        if len(self.category) == 1:
            raise InvalidLotError("A lot cannot be without a category")
        if category_id >= len(self.category):
            raise InvalidLotError("The parameter category_id is an invalid id")
        return self.category.pop(category_id)
