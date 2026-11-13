from dataclasses import dataclass
from desktop.modules.persons.core.errors import invalid_number_error
from desktop.modules.shared.value_objects.non_empty_string import NonEmptyString
from desktop.modules.persons.core.errors.invalid_number_error import InvalidNumberError


@dataclass(frozen=True)
class PhoneNumber:
    number: NonEmptyString
    country_code: NonEmptyString

    def __post_init__(self):
        if not isinstance(self.number, NonEmptyString):
            raise InvalidNumberError(
                "The type of the param number is invalid, must be an NonEmptyString object, not a ",
                self.number.__class__,
            )
        if not self.number.string.isnumeric():
            raise InvalidNumberError(
                "The param number is invalid, it has to be a number"
            )
        if len(self.number.string) != 10:
            raise InvalidNumberError(
                "The param number is invalid, it has to has 10 characters "
            )
        if not isinstance(self.country_code, NonEmptyString):
            raise InvalidNumberError(
                "The type of the param country_code is invalid, must be an NonEmptyString object, not a ",
                self.country_code.__class__,
            )
        if not self.country_code.string.isnumeric():
            raise InvalidNumberError("The param country_code must be a number")
        if len(self.country_code.string) > 3:
            raise InvalidNumberError(
                "The parameter country_code cannot be higher than 999"
            )
