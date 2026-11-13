from desktop.modules.persons.core.errors.invalid_email_error import InvalidEmailError
from desktop.modules.persons.core.errors.invalid_person_error import InvalidPersonError
from desktop.modules.persons.core.value_objects.phone_number import PhoneNumber
from desktop.modules.shared.entity import Entity
from desktop.modules.shared.value_objects.non_empty_string import NonEmptyString


class Person(Entity):
    def __init__(
        self,
        id: NonEmptyString,
        name: NonEmptyString,
        identification: NonEmptyString,
        email: NonEmptyString,
        phone_number: PhoneNumber,
        address: list[NonEmptyString],
    ) -> None:
        super().__init__(id)
        if not isinstance(name, NonEmptyString):
            raise InvalidPersonError(
                "The parameter name must be a NonEmptyString object, not a ",
                name.__class__,
            )
        if not isinstance(identification, NonEmptyString):
            raise InvalidPersonError(
                "The parameter identification must be a NonEmptyString object, not a ",
                identification.__class__,
            )
        if not identification.string.isnumeric():
            raise InvalidPersonError(
                "The parameter identification must be a numeric string"
            )
        if not isinstance(email, NonEmptyString):
            raise InvalidPersonError(
                "The parameter email must be a NonEmptyString object, not a",
                email.__class__,
            )
        if "@" not in email.string:
            raise InvalidPersonError("The parameter email is invalid")
        if not isinstance(phone_number, PhoneNumber):
            raise InvalidPersonError(
                "The parameter phone_number must be a PhoneNumber object, not a ",
                phone_number.__class__,
            )
        if not isinstance(address, list):
            raise InvalidPersonError(
                "The parameter address must be a list object, not a ", address.__class__
            )
        for add in address:
            if not isinstance(add, NonEmptyString):
                raise InvalidPersonError(
                    "The parameter address must be a list of NonEmptyString objects, not a list of ",
                    add.__class__,
                    " objects",
                )

        self.name = name
        self.identification = identification
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def change_email(self, new_email: str):
        email = NonEmptyString(new_email)
        if "@" not in email.string:
            raise InvalidEmailError("The email is invalid")
        self.email = email

    def change_phone_number(self, new_phone: str):
        phone = PhoneNumber(
            number=NonEmptyString(new_phone),
            country_code=self.phone_number.country_code,
        )
        self.phone_number = phone

    def add_address(self, new_address: str):
        address = NonEmptyString(new_address)
        self.address.append(address)

    def remove_address(self, id_address: int):
        if isinstance(id_address, bool) or not isinstance(id_address, int):
            raise InvalidPersonError(
                "The parameter id_address must be an integer object"
            )
        if id_address < 0:
            raise InvalidPersonError(
                "The parameter id_address must be greater or equals to zero"
            )
        if len(self.address) == 1:
            raise InvalidPersonError("A person cannot be without an address")
        if id_address >= len(self.address):
            raise InvalidPersonError("The parameter id_address is an invalid id")
        return self.address.pop(id_address)
