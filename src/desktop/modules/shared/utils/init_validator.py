from typing import get_origin, get_args, Union
from functools import wraps
import inspect
from types import UnionType


def _check_type(
    name: str, value: object, expected: type, error_cls: type[Exception]
) -> None:
    origin = get_origin(expected)
    args = get_args(expected)

    if origin in (Union, UnionType):
        if value is None and type(None) in args:
            return
        non_none_types = tuple(t for t in args if t is not type(None))
        for t in non_none_types:
            try:
                _check_type(name, value, t, error_cls)
                return
            except error_cls:
                continue
        raise error_cls(
            f"The parameter {name} must be {expected} object, not a {type(value)}"
        )

    if origin is list:
        if not isinstance(value, list):
            raise error_cls(
                f"The parameter {name} must be a list object, not a {type(value)}"
            )
        if args:
            item_type = args[0]
            for item in value:
                if not isinstance(item, item_type):
                    raise error_cls(
                        f"The parameter {name} must be a list of {item_type.__name__} objects, not of {type(item)}"
                    )
        return

    if expected is int and isinstance(value, bool):
        raise error_cls(f"The parameter {name} must be an int object, not a bool")

    if not isinstance(value, expected):
        raise error_cls(
            f"The parameter {name} must be a {expected.__name__} object, not a {type(value)}"
        )


def validate_init(error_cls: type[Exception]):
    def decorator(init_fn):
        sig = inspect.signature(init_fn)

        @wraps(init_fn)
        def wrapper(self, *args, **kwargs):
            bound = sig.bind(self, *args, **kwargs)
            bound.apply_defaults()

            for name, value in bound.arguments.items():
                if name == "self" or name == "id":
                    continue
                expected = sig.parameters[name].annotation
                if expected is inspect.Parameter.empty:
                    continue
                _check_type(name, value, expected, error_cls)
            return init_fn(self, *args, **kwargs)

        return wrapper

    return decorator
