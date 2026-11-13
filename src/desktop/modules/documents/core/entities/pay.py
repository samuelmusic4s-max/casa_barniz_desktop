from desktop.modules.documents.core.errors.invalid_pay_error import InvalidPayError
from desktop.modules.shared.entity import Entity
from desktop.modules.shared.utils import init_validator
from desktop.modules.shared.value_objects.money import Money
from desktop.modules.shared.value_objects.non_empty_string import NonEmptyString
from desktop.modules.shared.value_objects.timestamp import Timestamp


class Pay(Entity):
    @init_validator.validate_init(InvalidPayError)
    def __init__(
        self,
        id: NonEmptyString,
        url: NonEmptyString,
        is_advance: bool,
        amount: Money,
        method: NonEmptyString,
        timestamp: Timestamp,
    ) -> None:
        super().__init__(id)
        self.url = url
        self.is_advance = is_advance
        self.amount = amount
        self.method = method
        self.timestamp = timestamp
