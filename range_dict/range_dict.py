from range_dict.interval_tree import IntervalTree


class RangeDict(dict):
    __data__ = {
        "int": IntervalTree(),
        "float": IntervalTree(),
        "date": IntervalTree(),
        "datetime": IntervalTree(),
    }
