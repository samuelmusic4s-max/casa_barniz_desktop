from desktop.modules.persons.core.entities.person import Person
from desktop.modules.persons.core.errors.invalid_third_party_error import (
    InvalidThirdPartyError,
)
from desktop.modules.persons.core.value_objects.phone_number import PhoneNumber
from desktop.modules.shared.value_objects.non_empty_string import NonEmptyString


class ThirdParty(Person):
    def __init__(
        self,
        id: NonEmptyString,
        name: NonEmptyString,
        identification: NonEmptyString,
        email: NonEmptyString,
        phone_number: PhoneNumber,
        address: list[NonEmptyString],
        role: list[NonEmptyString],
    ) -> None:
        super().__init__(id, name, identification, email, phone_number, address)
        if not isinstance(role, list):
            raise InvalidThirdPartyError(
                "The param role must be a list, not a ", role.__class__
            )
        for r in role:
            if not isinstance(r, NonEmptyString):
                raise InvalidThirdPartyError(
                    "The role must be a list of NonEmptyString objects, not of ",
                    r.__class__,
                )
        self.role = role

    def add_role(self, new_role: str):
        role = NonEmptyString(new_role)
        self.role.append(role)

    def remove_role(self, id_role: int):
        if isinstance(id_role, bool) or not isinstance(id_role, int):
            raise InvalidThirdPartyError(
                "The parameter id_role must be an integer object"
            )
        if id_role < 0:
            raise InvalidThirdPartyError(
                "The parameter id_role must be greater or equals to zero"
            )
        if len(self.role) == 1:
            raise InvalidThirdPartyError("A third party cannot be without an role")
        if id_role >= len(self.role):
            raise InvalidThirdPartyError("The parameter id_role is an invalid id")
        return self.role.pop(id_role)
