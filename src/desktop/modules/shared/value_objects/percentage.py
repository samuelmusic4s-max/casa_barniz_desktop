from dataclasses import dataclass

from desktop.modules.shared.errors.invalid_percentage_error import (
    InvalidPercentageError,
)


@dataclass(frozen=True)
class Percentage:
    value: int

    def __post_init__(self):
        if not isinstance(self.value, int) or isinstance(self.value, bool):
            raise InvalidPercentageError("The percentage must be an integer value")
        if self.value < 0:
            raise InvalidPercentageError(
                "The percentage must be greater or equals to 0"
            )
