import pytest
from desktop.modules.shared.value_objects.money import Money
from desktop.modules.shared.errors.invalid_quantity_money_error import (
    InvalidQuantityMoneyError,
)


@pytest.fixture
def money_generic():
    return Money(10000)


def test_creating_money(money_generic):
    money = money_generic
    assert money == Money(10000)


@pytest.mark.parametrize("invalid_quantity_money", [-50000, 3.8, True, "hola", [5]])
def test_creating_money_error(invalid_quantity_money):
    with pytest.raises(InvalidQuantityMoneyError):
        Money(invalid_quantity_money)


def test_adding_money(money_generic):
    money = money_generic
    assert money.add_money(5000) == Money(15000)


@pytest.mark.parametrize("invalid_quantity_money_adding", [-10, 3.8, True])
def test_adding_money_error(invalid_quantity_money_adding, money_generic):
    money = money_generic
    with pytest.raises(InvalidQuantityMoneyError):
        money.add_money(invalid_quantity_money_adding)


def test_removing_money(money_generic):
    money = money_generic
    assert money.remove_money(5000) == Money(5000)


@pytest.mark.parametrize("invalid_quantity_money_removing", [-10, 3.8, 15000])
def test_removing_money_error(invalid_quantity_money_removing, money_generic):
    money = money_generic
    with pytest.raises(InvalidQuantityMoneyError):
        money.remove_money(invalid_quantity_money_removing)
