from desktop.modules.shared.value_objects.non_empty_string import NonEmptyString
from desktop.modules.shared.errors.invalid_string_error import InvalidStringError


class Entity:
    def __init__(self, id: NonEmptyString) -> None:
        if not isinstance(id, NonEmptyString):
            raise InvalidStringError(
                "The id of the entity ", self.__class__, " must be an NonEmptyString"
            )
        self.id = id

    def __eq__(self, value: object) -> bool:
        return isinstance(value, self.__class__) and self.id == value.id

    def __hash__(self) -> int:
        return hash(self.id)
