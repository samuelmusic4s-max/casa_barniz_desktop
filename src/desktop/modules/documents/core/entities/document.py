from desktop.modules.documents.core.errors.invalid_document_error import (
    InvalidDocumentError,
)
from desktop.modules.shared.entity import Entity


from desktop.modules.shared.value_objects.non_empty_string import NonEmptyString
from desktop.modules.shared.value_objects.timestamp import Timestamp


class Document(Entity):
    def __init__(
        self,
        id: NonEmptyString,
        person_id: NonEmptyString,
        consecutive: NonEmptyString,
        timestamp: Timestamp,
        observations: NonEmptyString,
        status: NonEmptyString,
    ) -> None:
        super().__init__(id)
        if not isinstance(person_id, NonEmptyString):
            raise InvalidDocumentError(
                "The parameter person_id must be a NonEmptyString object, not a ",
                person_id.__class__,
            )
        if not isinstance(consecutive, NonEmptyString):
            raise InvalidDocumentError(
                "The parameter consecutive must be a NonEmptyString object, not a ",
                consecutive.__class__,
            )
        if not isinstance(timestamp, Timestamp):
            raise InvalidDocumentError(
                "The parameter timestamp must be a Timestamp object, not a ",
                timestamp.__class__,
            )
        if not isinstance(observations, NonEmptyString):
            raise InvalidDocumentError(
                "The parameter observations must be a NonEmptyString object, not a ",
                observations.__class__,
            )
        if not isinstance(status, NonEmptyString):
            raise InvalidDocumentError(
                "The parameter status must be a NonEmptyString object, not a ",
                status.__class__,
            )
        self.person_id = person_id
        self.consecutive = consecutive
        self.timestamp = timestamp
        self.observations = observations
        self.status = status

    def change_observations(self, new_observations: str):
        observations = NonEmptyString(new_observations)
        self.observations = observations
