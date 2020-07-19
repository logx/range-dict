from datetime import date, datetime
from typing import TypeVar, Any, Tuple, Union

from range_dict.interval_tree import IntervalTree

T = TypeVar('T', int, float, date, datetime, Any)


class RangeDict:
    def __init__(self):
        self._buckets = {
            "int": IntervalTree(),
            "float": IntervalTree(),
            "date": IntervalTree(),
            "datetime": IntervalTree(),
        }

    def __setitem__(self, key: Union[T, Tuple[T, T]], value: Any) -> None:
        lower_key, higher_key = _format_key(key)
        key = (lower_key, higher_key)

        bucket = type(lower_key).__name__
        # User defined bucket, create new Interval Tree
        if bucket not in self._buckets:
            self._buckets[bucket] = IntervalTree()

        self._buckets[bucket].insert(key, value)

    def __getitem__(self, key: Union[T, Tuple[T, T]]) -> Any:
        lower_key, higher_key = _format_key(key)
        key = (lower_key, higher_key)

        bucket = type(lower_key).__name__
        if bucket not in self._buckets:
            raise KeyError(f"No range for given type: '{bucket}'")

        # Mimic 'dict' behavior
        result = self._buckets[bucket].find(key)
        if not result:
            raise KeyError(f"No value for key: '{key}'")
        return result

    def __delitem__(self, key: Union[T, Tuple[T, T]]):  # pragma: no cover
        raise NotImplementedError

    def __len__(self):  # pragma: no cover
        raise NotImplementedError

    def get(self, key: Union[T, Tuple[T, T]], default=None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def items(self):  # pragma: no cover
        raise NotImplementedError

    def keys(self):  # pragma: no cover
        raise NotImplementedError

    def values(self):  # pragma: no cover
        raise NotImplementedError

    def update(self):  # pragma: no cover
        raise NotImplementedError

    def setdefault(self):  # pragma: no cover
        raise NotImplementedError

    def clear(self):  # pragma: no cover
        raise NotImplementedError


def _format_key(key: Union[T, Tuple[T, T]]) -> Tuple[T, T]:  # type: ignore
    # Key is a single value, it needs to be transformed to tuple
    if type(key) not in (tuple, list):  # type: ignore
        return key, key  # type: ignore

    if type(key) in (tuple, list) and len(key) != 2:  # type: ignore
        raise KeyError(f"Range requires 2 elements, got {len(key)}: '{key}'")  # type: ignore

    return key  # type: ignore
