from datetime import date, datetime

import pytest

from range_dict import RangeDict


def test_available_range_for_key_returns_value():
    months = RangeDict()

    months[date(2020, 1, 1), date(2020, 1, 31)] = "January"

    assert months[date(2020, 1, 12)] == "January"


def test_missing_range_for_key_raises_error():
    months = RangeDict()

    months[date(2020, 1, 1), date(2020, 1, 31)] = "January"

    with pytest.raises(KeyError):
        _ = months[date(2020, 6, 6)]


@pytest.mark.parametrize(
    "range_start, range_end, value, key, expected_value",
    [
        (datetime(2020, 1, 1, 16, 0), datetime(2020, 1, 1, 20, 0), "evening", datetime(2020, 1, 1, 16, 0), "evening"),
        (datetime(2020, 1, 1, 16, 0), datetime(2020, 1, 1, 20, 0), "evening", datetime(2020, 1, 1, 18, 0), "evening"),
        (datetime(2020, 1, 1, 16, 0), datetime(2020, 1, 1, 20, 0), "evening", datetime(2020, 1, 1, 20, 0), "evening"),
        (datetime(2020, 1, 1, 16, 0), datetime(2020, 1, 1, 20, 0), "evening", datetime(2020, 1, 1, 22, 0), None),
    ]
)
def test_datetime_as_key(range_start, range_end, value, key, expected_value):
    day = RangeDict()

    day[range_start, range_end] = value

    assert day.get(key) == expected_value


@pytest.mark.parametrize(
    "first_range, first_value, second_range, second_value, key, expected_value",
    [
        ((date(2020, 7, 1), date(2020, 7, 14)), "John's holidays", (date(2020, 7, 10), date(2020, 7, 20)), "Mary's holidays", date(2020, 7, 12), ["John's holidays", "Mary's holidays"]),  # noqa: E221, E501
        ((date(2020, 7, 1), date(2020, 7, 14)), "John's holidays", (date(2020, 7, 10), date(2020, 7, 20)), "Mary's holidays", date(2020, 7, 14), ["John's holidays", "Mary's holidays"]),  # noqa: E221, E501
        ((date(2020, 7, 1), date(2020, 7, 14)), "John's holidays", (date(2020, 7, 10), date(2020, 7, 20)), "Mary's holidays", date(2020, 7, 1),  "John's holidays"),                       # noqa: E221, E501
        ((date(2020, 7, 1), date(2020, 7, 14)), "John's holidays", (date(2020, 7, 10), date(2020, 7, 20)), "Mary's holidays", date(2020, 7, 20), "Mary's holidays"),                       # noqa: E221, E501
        ((date(2020, 7, 1), date(2020, 7, 14)), "John's holidays", (date(2020, 7, 10), date(2020, 7, 20)), "Mary's holidays", date(2020, 8, 30), None),                                    # noqa: E221, E501
    ]
)
def test_overlapping_ranges(first_range, first_value, second_range, second_value, key, expected_value):
    holidays = RangeDict()

    holidays[first_range] = first_value
    holidays[second_range] = second_value

    assert holidays.get(key) == expected_value
