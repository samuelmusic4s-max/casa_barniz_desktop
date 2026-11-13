from desktop.modules.documents.core.entities.pay import Pay
from desktop.modules.shared.value_objects.money import Money
from desktop.modules.shared.value_objects.non_empty_string import NonEmptyString
from desktop.modules.shared.value_objects.timestamp import Timestamp


class EmittedPay(Pay):
    def __init__(
        self,
        id: NonEmptyString,
        url: NonEmptyString,
        is_advance: bool,
        amount: Money,
        method: NonEmptyString,
        timestamp: Timestamp,
    ) -> None:
        super().__init__()
