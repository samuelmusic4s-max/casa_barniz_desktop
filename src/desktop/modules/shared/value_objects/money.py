from desktop.modules.shared.errors.invalid_quantity_money_error import (
    InvalidQuantityMoneyError,
)
from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    quantity: int

    def __post_init__(self):
        if isinstance(self.quantity, bool) or not isinstance(self.quantity, int):
            raise InvalidQuantityMoneyError("The money must be an integer quantity")
        if self.quantity < 0:
            raise InvalidQuantityMoneyError(
                "The money must be greater or equal to zero"
            )

    def add_money(self, newMoney: int):
        mon = Money(newMoney)
        return Money(self.quantity + mon.quantity)

    def remove_money(self, money: int):
        mon = Money(money)
        return Money(self.quantity - mon.quantity)
