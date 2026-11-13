from desktop.modules.shared.errors.invalid_quantity_stock_error import (
    InvalidQuantityStockError,
)
from desktop.modules.shared.errors.invalid_operation_error import InvalidOperationError
from dataclasses import dataclass


@dataclass(frozen=True)
class Stock:
    quantity: int

    def __post_init__(self):
        if isinstance(self.quantity, bool) or not isinstance(self.quantity, int):
            raise InvalidQuantityStockError("A quantity of stock must be an integer")
        if self.quantity < 0:
            raise InvalidQuantityStockError(
                "A quantity of stock must be greater or equal than zero"
            )

    def add_stock(self, new_stock: Stock | int) -> Stock:
        if not isinstance(new_stock, Stock) and not isinstance(new_stock, int):
            raise InvalidOperationError(
                f"Cannot add an object type {new_stock.__class__} to stock"
            )
        number = new_stock if isinstance(new_stock, int) else new_stock.quantity
        if number <= 0:
            raise InvalidOperationError(
                "Cannot add to stock a quantity equals or less than zero"
            )
        value = Stock(new_stock) if isinstance(new_stock, int) else new_stock
        return Stock(self.quantity + value.quantity)

    def remove_stock(self, stock: Stock | int) -> Stock:
        if not isinstance(stock, Stock) and not isinstance(stock, int):
            raise InvalidOperationError(
                f"Cannot add an object type {stock.__class__} to stock"
            )
        number = stock if isinstance(stock, int) else stock.quantity
        if number <= 0:
            raise InvalidOperationError(
                "Cannot remove from stock a quantity equals or less than zero"
            )
        value = Stock(stock) if isinstance(stock, int) else stock
        return Stock(self.quantity - value.quantity)
