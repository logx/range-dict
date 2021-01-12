from datetime import datetime

import pytest

from range_dict import RangeDict

KEY_0 = datetime(2021, 1, 12), datetime(2021, 1, 22)
KEY_1 = 0, 100
KEY_2 = 5, 200

VAL = "some value"


@pytest.mark.parametrize(
    "initial_dict, expected_keys", [
        ({},                       []),
        ({KEY_0: VAL},             [KEY_0]),
        # Order of the keys of different type does not depend on order of insertion
        ({KEY_0: VAL, KEY_1: VAL}, [KEY_1, KEY_0]),
        ({KEY_1: VAL, KEY_0: VAL}, [KEY_1, KEY_0]),
        ({KEY_1: VAL, KEY_2: VAL}, [KEY_1, KEY_2]),
        ({KEY_2: VAL, KEY_1: VAL}, [KEY_2, KEY_1]),
    ]
)
def test_get_keys(initial_dict, expected_keys):
    assert RangeDict(initial_dict).keys() == expected_keys


@pytest.mark.parametrize(
    "initial_dict, expected_length", [
        ({},                                   0),
        ({KEY_0: VAL},                         1),
        ({KEY_0: VAL, KEY_1: VAL},             2),
        ({KEY_1: VAL, KEY_2: VAL},             2),
        ({KEY_0: VAL, KEY_1: VAL, KEY_2: VAL}, 3),
    ]
)
def test_length(initial_dict, expected_length):
    assert len(RangeDict(initial_dict)) == expected_length
