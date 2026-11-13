from desktop.modules.shared.errors.empty_string_error import EmptyStringError
from dataclasses import dataclass


@dataclass(frozen=True)
class NonEmptyString:
    string: str

    def __post_init__(self):
        if not isinstance(self.string, str):
            raise EmptyStringError("The value with name string must be a string")
        if self.string.strip() == "":
            raise EmptyStringError("The string cannot be empty")
