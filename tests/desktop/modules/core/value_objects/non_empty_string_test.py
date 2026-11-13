from desktop.modules.shared.value_objects.non_empty_string import NonEmptyString
from desktop.modules.shared.errors.empty_string_error import EmptyStringError
import pytest


@pytest.fixture
def generic_string() -> NonEmptyString:
    return NonEmptyString("Hello World")


def test_creating_string(generic_string):
    assert generic_string.string == "Hello World"


@pytest.mark.parametrize("invalid_values", ["   ", "", True, 5, ["h"], 3.8])
def test_creating_string_error(invalid_values):
    with pytest.raises(EmptyStringError):
        NonEmptyString(invalid_values)
