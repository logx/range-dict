# flake8: noqa: E221, E501
from datetime import date, datetime

import pytest

from range_dict import RangeDict

# This file contains all test related to **fetching** data from the dictionary.


@pytest.mark.parametrize(
    "range_key, range_value, key",
    [
        ((date(2020, 1, 1),            date(2020, 1, 31)),           "January",             date(2020, 1, 1)),
        ((date(2020, 1, 1),            date(2020, 1, 31)),           "January",             date(2020, 1, 12)),
        ((date(2020, 1, 1),            date(2020, 1, 31)),           "January",             date(2020, 1, 31)),
        ((datetime(2020, 1, 1, 16, 0), datetime(2020, 1, 1, 20, 0)), "evening",             datetime(2020, 1, 1, 16, 0)),
        ((datetime(2020, 1, 1, 16, 0), datetime(2020, 1, 1, 20, 0)), "evening",             datetime(2020, 1, 1, 18, 0)),
        ((datetime(2020, 1, 1, 16, 0), datetime(2020, 1, 1, 20, 0)), "evening",             datetime(2020, 1, 1, 20, 0)),
        ((1000,                        2000),                        "low_income",          1000),
        ((1000,                        2000),                        "low_income",          1200),
        ((1000,                        2000),                        "low_income",          2000),
        ((36.4,                        37.6),                        "body_temperature_ok", 36.4),
        ((36.4,                        37.6),                        "body_temperature_ok", 36.6),
        ((36.4,                        37.6),                        "body_temperature_ok", 37.6),
    ]
)
def test_available_range_for_key_returns_value(range_key, range_value, key):
    data = RangeDict({range_key: range_value})

    assert data[key] == [range_value]


@pytest.mark.parametrize(
    "range_key, key",
    [
        ((date(2020, 1, 1),            date(2020, 1, 31)),           date(2020, 3, 1)),
        ((datetime(2020, 1, 1, 16, 0), datetime(2020, 1, 1, 20, 0)), datetime(2020, 1, 1, 22, 0)),
        ((datetime(2020, 1, 1, 16, 0), datetime(2020, 1, 1, 20, 0)), datetime(2020, 1, 2, 18, 0)),
        ((1000,                        2000),                        3000),
        ((36.4,                        37.6),                        38.4),
    ]
)
def test_missing_range_for_key_raises_error(range_key, key):
    data = RangeDict({range_key: "some_value"})

    with pytest.raises(KeyError):
        _ = data[key]


@pytest.mark.parametrize(
    "range_key, key",
    [
        ((date(2020, 1, 1),            date(2020, 1, 31)),           date(2020, 4, 1)),
        ((datetime(2020, 1, 1, 16, 0), datetime(2020, 1, 1, 20, 0)), datetime(2020, 1, 1, 23, 0)),
        ((datetime(2020, 1, 1, 16, 0), datetime(2020, 1, 1, 20, 0)), datetime(2020, 1, 4, 18, 0)),
        ((1000,                        2000),                        500),
        ((36.4,                        37.6),                        35.4),
    ]
)
def test_missing_range_for_key_returns_none(range_key, key):
    data = RangeDict()

    data[range_key] = "some_value"

    assert data.get(key) is None


JOHN_MARY_HOLIDAYS = (
    (date(2020, 7, 1),  date(2020, 7, 14)), "John's holidays",
    (date(2020, 7, 10), date(2020, 7, 20)), "Mary's holidays"
)

TV_PROGRAM = (
    (datetime(2020, 7, 12, 14, 15), datetime(2020, 7, 12, 16, 10)), "Spider-Man: Into the Spider-Verse on HBO",
    (datetime(2020, 7, 12, 14, 10), datetime(2020, 7, 12, 15, 0)),  "Doctor Who on BBC"
)

# In PLN
SALARIES = (
    (4000, 8000),  "Software Engineer at XYZ Inc.",
    (6000, 10000), "Software Engineer at ABC Inc."
)

# In PLN
PRICES = (
    (3277.50, 5418.90), "Galaxy S20",
    (4499.99, 5490.10), "iPhone 11 Pro"
)


@pytest.mark.parametrize(
    "first_range, first_value, second_range, second_value, key, expected_value",
    [
        (*JOHN_MARY_HOLIDAYS, date(2020, 7, 10),             ["John's holidays", "Mary's holidays"]),
        (*JOHN_MARY_HOLIDAYS, date(2020, 7, 12),             ["John's holidays", "Mary's holidays"]),
        (*JOHN_MARY_HOLIDAYS, date(2020, 7, 14),             ["John's holidays", "Mary's holidays"]),
        (*JOHN_MARY_HOLIDAYS, date(2020, 7, 1),              ["John's holidays"]),
        (*JOHN_MARY_HOLIDAYS, date(2020, 7, 20),             ["Mary's holidays"]),
        (*JOHN_MARY_HOLIDAYS, date(2020, 8, 30),             None),
        (*TV_PROGRAM,         datetime(2020, 7, 12, 14, 30), ["Spider-Man: Into the Spider-Verse on HBO", "Doctor Who on BBC"]),
        (*TV_PROGRAM,         datetime(2020, 7, 12, 15, 0),  ["Spider-Man: Into the Spider-Verse on HBO", "Doctor Who on BBC"]),
        (*TV_PROGRAM,         datetime(2020, 7, 12, 14, 10), ["Doctor Who on BBC"]),
        (*TV_PROGRAM,         datetime(2020, 7, 12, 15, 30), ["Spider-Man: Into the Spider-Verse on HBO"]),
        (*TV_PROGRAM,         datetime(2020, 7, 12, 16, 10), ["Spider-Man: Into the Spider-Verse on HBO"]),
        (*TV_PROGRAM,         datetime(2020, 7, 12, 20, 0),  None),
        (*SALARIES,           6000,                          ["Software Engineer at XYZ Inc.", "Software Engineer at ABC Inc."]),
        (*SALARIES,           8000,                          ["Software Engineer at XYZ Inc.", "Software Engineer at ABC Inc."]),
        (*SALARIES,           4000,                          ["Software Engineer at XYZ Inc."]),
        (*SALARIES,           10000,                         ["Software Engineer at ABC Inc."]),
        (*SALARIES,           12000,                         None),
        (*PRICES,             5000.0,                        ["Galaxy S20", "iPhone 11 Pro"]),
        (*PRICES,             4499.99,                       ["Galaxy S20", "iPhone 11 Pro"]),
        (*PRICES,             3277.50,                       ["Galaxy S20"]),
        (*PRICES,             5490.10,                       ["iPhone 11 Pro"]),
        (*PRICES,             2999.99,                       None),
    ]
)
def test_overlapping_ranges(first_range, first_value, second_range, second_value, key, expected_value):
    data = RangeDict()

    data[first_range] = first_value
    data[second_range] = second_value

    assert data.get(key) == expected_value
