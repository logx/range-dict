# flake8: noqa: E221, E501

import pytest

from range_dict.interval_tree import IntervalTree


@pytest.mark.parametrize(
    "input_data, range_key, expected_value", [
        ([((10, 30), 'A'), ((15, 25), 'B'), ((20, 30), 'C')], (0,  9),  []),
        ([((10, 30), 'A'), ((15, 25), 'B'), ((20, 30), 'C')], (10, 14), ['A']),
        ([((10, 30), 'A'), ((15, 25), 'B'), ((20, 30), 'C')], (15, 15), ['A', 'B']),
        ([((10, 30), 'A'), ((15, 25), 'B'), ((20, 30), 'C')], (10, 15), ['A', 'B']),
        ([((10, 30), 'A'), ((15, 25), 'B'), ((20, 30), 'C')], (0,  60), ['A', 'B', 'C']),
    ]
)
def test_tree(input_data, range_key, expected_value):
    tree = IntervalTree()

    for input_range_key, input_value in input_data:
        tree.insert(input_range_key, input_value)

    assert tree.find(range_key) == expected_value
