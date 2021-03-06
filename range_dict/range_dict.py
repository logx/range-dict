from collections import defaultdict
from datetime import date, datetime
from typing import TypeVar, Any, Tuple, Union, List, Dict, Optional

from range_dict.interval_tree import IntervalTree

T = TypeVar('T', int, float, date, datetime, Any)

RangeDictKey = Union[T, Tuple[T, T]]
InitialRangeDict = Dict[RangeDictKey, Any]


class RangeDict:
    def __init__(self, initial_dict: Optional[InitialRangeDict] = None):
        self._buckets: Dict[str, IntervalTree] = defaultdict(IntervalTree)

        if initial_dict:
            for key, value in initial_dict.items():
                self.__setitem__(key, value)

    def __setitem__(self, key: RangeDictKey, value: Any) -> None:
        lower_key, higher_key = _format_key(key)
        key = (lower_key, higher_key)

        self._buckets[type(lower_key).__name__].insert(key, value)

    def __getitem__(self, key: RangeDictKey) -> Any:
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

    def __delitem__(self, key: RangeDictKey):  # pragma: no cover
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self.keys())

    def get(self, key: RangeDictKey, default=None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def items(self):  # pragma: no cover
        raise NotImplementedError

    def keys(self) -> List[Any]:
        keys = []

        for interval_tree in self._buckets.values():
            keys += interval_tree.keys()

        return keys

    def values(self):  # pragma: no cover
        raise NotImplementedError

    def update(self):  # pragma: no cover
        raise NotImplementedError

    def setdefault(self):  # pragma: no cover
        raise NotImplementedError

    def clear(self):  # pragma: no cover
        raise NotImplementedError


def _format_key(key: RangeDictKey) -> Tuple[T, T]:  # type: ignore
    # Key is a single value, it needs to be transformed to tuple
    if type(key) not in (tuple, list):  # type: ignore
        return key, key  # type: ignore

    if type(key) in (tuple, list) and len(key) != 2:  # type: ignore
        raise KeyError(f"Range requires 2 elements, got {len(key)}: '{key}'")  # type: ignore

    return key  # type: ignore
