from desktop.modules.shared.value_objects import stock
import pytest
from desktop.modules.shared.value_objects.stock import Stock
from desktop.modules.shared.errors.invalid_operation_error import InvalidOperationError
from desktop.modules.shared.errors.invalid_quantity_stock_error import (
    InvalidQuantityStockError,
)


@pytest.fixture
def stock_data():
    stock = {
        "initial": 9,
        "add": 5,
        "add_err": -1,
        "remove": 5,
        "remove_err": -10,
        "remove_err2": 10,
    }
    return stock


@pytest.fixture
def generic_stock():
    return Stock(9)


def test_creating_stock(stock_data):
    stock = Stock(9)
    assert stock.quantity == stock_data["initial"]


@pytest.mark.parametrize("invalid_quantity", [9.8, -1, True, False, "5"])
def test_creating_stock_error(invalid_quantity):
    with pytest.raises(InvalidQuantityStockError):
        Stock(invalid_quantity)


def test_adding_stock(generic_stock, stock_data):
    stock = generic_stock
    new_stock = stock.add_stock(stock_data["add"])
    assert new_stock.quantity == 14


@pytest.mark.parametrize("invalid_quantity_add", [-1, 0])
def test_adding_stock_error(generic_stock, invalid_quantity_add):
    stock = generic_stock
    with pytest.raises(InvalidOperationError):
        stock.add_stock(invalid_quantity_add)


def test_removing_stock(generic_stock, stock_data):
    stock = generic_stock
    new_stock = stock.remove_stock(stock_data["remove"])
    assert new_stock.quantity == 4


@pytest.mark.parametrize("invalid_quantity_remove", [0, -10])
def test_removing_stock_err(generic_stock, invalid_quantity_remove):
    stock = generic_stock
    with pytest.raises(InvalidOperationError):
        stock.remove_stock(invalid_quantity_remove)

    with pytest.raises(InvalidQuantityStockError):
        stock.remove_stock(10)
