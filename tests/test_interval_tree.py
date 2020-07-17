# flake8: noqa: E221, E501
from datetime import date, datetime

import pytest

from range_dict.interval_tree import IntervalTree


@pytest.mark.parametrize(
    "input_data, range_key, expected_value", [
        # integer as range_key
        ([((10, 30), 'A'),                                       ((15, 25), 'B'),                                       ((20, 30), 'C')],                                       (0,  9),                                         []),
        ([((10, 30), 'A'),                                       ((15, 25), 'B'),                                       ((20, 30), 'C')],                                       (10, 14),                                        ['A']),
        ([((10, 30), 'A'),                                       ((15, 25), 'B'),                                       ((20, 30), 'C')],                                       (15, 15),                                        ['A', 'B']),
        ([((10, 30), 'A'),                                       ((15, 25), 'B'),                                       ((20, 30), 'C')],                                       (10, 15),                                        ['A', 'B']),
        ([((10, 30), 'A'),                                       ((15, 25), 'B'),                                       ((20, 30), 'C')],                                       (0,  60),                                        ['A', 'B', 'C']),
        # float as range_key
        ([((10.0, 30.0), 'A'),                                   ((15.0, 25.0), 'B'),                                   ((20.0, 30.0), 'C')],                                   (0.0,  9.0),                                     []),
        ([((10.0, 30.0), 'A'),                                   ((15.0, 25.0), 'B'),                                   ((20.0, 30.0), 'C')],                                   (10.0, 14.0),                                    ['A']),
        ([((10.0, 30.0), 'A'),                                   ((15.0, 25.0), 'B'),                                   ((20.0, 30.0), 'C')],                                   (15.0, 15.0),                                    ['A', 'B']),
        ([((10.0, 30.0), 'A'),                                   ((15.0, 25.0), 'B'),                                   ((20.0, 30.0), 'C')],                                   (10.0, 15.0),                                    ['A', 'B']),
        ([((10.0, 30.0), 'A'),                                   ((15.0, 25.0), 'B'),                                   ((20.0, 30.0), 'C')],                                   (0.0,  60.0),                                    ['A', 'B', 'C']),
        # integer as range_key, but with lists as values
        ([((10, 30), ['A']),                                     ((15, 25), ['B']),                                     ((20, 30), ['C'])],                                     (0,  9),                                         []),
        ([((10, 30), ['A']),                                     ((15, 25), ['B']),                                     ((20, 30), ['C'])],                                     (10, 14),                                        [['A']]),
        ([((10, 30), ['A']),                                     ((15, 25), ['B']),                                     ((20, 30), ['C'])],                                     (15, 15),                                        [['A'], ['B']]),
        ([((10, 30), ['A']),                                     ((15, 25), ['B']),                                     ((20, 30), ['C'])],                                     (10, 15),                                        [['A'], ['B']]),
        ([((10, 30), ['A']),                                     ((15, 25), ['B']),                                     ((20, 30), ['C', 'D'])],                                (0,  60),                                        [['A'], ['B'], ['C', 'D']]),
        # date as range_key
        ([((date(2020, 1, 10), date(2020, 1, 30)), 'A'),         ((date(2020, 1, 15), date(2020, 1, 25)), 'B'),         ((date(2020, 1, 20), date(2020, 1, 30)), 'C')],         (date(2020, 1, 1),   date(2020, 1, 9)),          []),
        ([((date(2020, 1, 10), date(2020, 1, 30)), 'A'),         ((date(2020, 1, 15), date(2020, 1, 25)), 'B'),         ((date(2020, 1, 20), date(2020, 1, 30)), 'C')],         (date(2020, 1, 10),  date(2020, 1, 14)),         ['A']),
        ([((date(2020, 1, 10), date(2020, 1, 30)), 'A'),         ((date(2020, 1, 15), date(2020, 1, 25)), 'B'),         ((date(2020, 1, 20), date(2020, 1, 30)), 'C')],         (date(2020, 1, 15),  date(2020, 1, 15)),         ['A', 'B']),
        ([((date(2020, 1, 10), date(2020, 1, 30)), 'A'),         ((date(2020, 1, 15), date(2020, 1, 25)), 'B'),         ((date(2020, 1, 20), date(2020, 1, 30)), 'C')],         (date(2020, 1, 10),  date(2020, 1, 15)),         ['A', 'B']),
        ([((date(2020, 1, 10), date(2020, 1, 30)), 'A'),         ((date(2020, 1, 15), date(2020, 1, 25)), 'B'),         ((date(2020, 1, 20), date(2020, 1, 30)), 'C')],         (date(2020, 1, 10),  date(2020, 1, 30)),         ['A', 'B', 'C']),
        # datetime as range_key
        ([((datetime(2020, 1, 10), datetime(2020, 1, 30)), 'A'), ((datetime(2020, 1, 15), datetime(2020, 1, 25)), 'B'), ((datetime(2020, 1, 20), datetime(2020, 1, 30)), 'C')], (datetime(2020, 1, 1),   datetime(2020, 1, 9)),  []),
        ([((datetime(2020, 1, 10), datetime(2020, 1, 30)), 'A'), ((datetime(2020, 1, 15), datetime(2020, 1, 25)), 'B'), ((datetime(2020, 1, 20), datetime(2020, 1, 30)), 'C')], (datetime(2020, 1, 10),  datetime(2020, 1, 14)), ['A']),
        ([((datetime(2020, 1, 10), datetime(2020, 1, 30)), 'A'), ((datetime(2020, 1, 15), datetime(2020, 1, 25)), 'B'), ((datetime(2020, 1, 20), datetime(2020, 1, 30)), 'C')], (datetime(2020, 1, 15),  datetime(2020, 1, 15)), ['A', 'B']),
        ([((datetime(2020, 1, 10), datetime(2020, 1, 30)), 'A'), ((datetime(2020, 1, 15), datetime(2020, 1, 25)), 'B'), ((datetime(2020, 1, 20), datetime(2020, 1, 30)), 'C')], (datetime(2020, 1, 10),  datetime(2020, 1, 15)), ['A', 'B']),
        ([((datetime(2020, 1, 10), datetime(2020, 1, 30)), 'A'), ((datetime(2020, 1, 15), datetime(2020, 1, 25)), 'B'), ((datetime(2020, 1, 20), datetime(2020, 1, 30)), 'C')], (datetime(2020, 1, 10),  datetime(2020, 1, 30)), ['A', 'B', 'C']),
    ]
)
def test_tree(input_data, range_key, expected_value):
    tree = IntervalTree()

    for input_range_key, input_value in input_data:
        tree.insert(input_range_key, input_value)

    assert tree.find(range_key) == expected_value


@pytest.mark.parametrize(
    "range_key", [
        (10,    date(2020, 7, 17)),
        (10,    datetime(2020, 7, 17)),
        (10.4,  date(2020, 7, 17)),
        (10.4,  datetime(2020, 7, 17)),
        (10.4,  datetime(2020, 7, 17)),
        ("str", 10),
        ("str", 10.4),
        ("str", date(2020, 7, 17)),
        ("str", datetime(2020, 7, 17)),
    ]
)
def test_illegal_range_raises_error(range_key):
    tree = IntervalTree()

    with pytest.raises(KeyError):
        tree.insert(range_key, "whatever")


@pytest.mark.parametrize(
    "range_key", [
        (10,                   1),
        (10.0,                 1.0),
        (date(2020, 1, 1),     date(1997, 1, 1)),
        (datetime(2020, 1, 1), datetime(1997, 1, 1))
    ]
)
def test_sort_range(range_key, caplog):
    tree = IntervalTree()

    tree.insert(range_key, "whatever")

    assert "Inverting order of keys passed to Range Dict's Interval Tree" in caplog.text
