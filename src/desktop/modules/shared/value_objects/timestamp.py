from dataclasses import dataclass
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from desktop.modules.shared.errors.invalid_datetime_error import InvalidDatetimeError

BOGOTA_TZ = ZoneInfo("America/Bogota")
TIME_MIN = datetime(2012, 1, 1).astimezone(BOGOTA_TZ)


@dataclass(frozen=True)
class Timestamp:
    value: datetime

    def __post_init__(self):
        TIME_MAX = datetime.now(BOGOTA_TZ) + timedelta(weeks=4)
        if not isinstance(self.value, datetime):
            raise InvalidDatetimeError(
                "The datetime must be a datetime, not a ", self.value.__class__
            )
        if self.value.tzinfo is None or self.value.tzinfo.utcoffset(self.value) is None:
            raise InvalidDatetimeError("The datetime must has timezone")
        if self.value < TIME_MIN:
            raise InvalidDatetimeError(
                "The datetime is invalid, it must be greater than 2012"
            )
        if self.value > TIME_MAX:
            raise InvalidDatetimeError(
                "The datetime cannot be greater than one month in the future"
            )

        object.__setattr__(self, "value", self.value.astimezone(BOGOTA_TZ))
