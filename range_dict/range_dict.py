from collections import UserDict

from range_dict.interval_tree import IntervalTree


class RangeDict(UserDict):
    __data__ = {
        "int": IntervalTree(),
        "float": IntervalTree(),
        "date": IntervalTree(),
    }
