from race_average import *
import pytest


def test_parse_date():
    assert parse_date("08:30 AM, DAY 2") == (8, 30, True, 2)
    assert parse_date("07:59 PM, DAY 4") == (7, 59, False, 4)
    assert parse_date("7:08 PM, DAY 4") == (7, 8, False, 4)
    with pytest.raises(ValueError):
        parse_date("07:30 AM DAY 1")
        parse_date("5:89 PM, DAY 2")
        parse_date("24:30 AM, DAY 2")


def test_get_minutes_per_race():
    assert get_minutes_per_race("08:30 AM, DAY 2") == 1470
    assert get_minutes_per_race("9:30 PM, DAY 10") == 13770
    assert get_minutes_per_race("8:00 AM, DAY 10") == 12960
    assert get_minutes_per_race("12:00 PM, DAY 2") == 1680
    assert get_minutes_per_race("12:00 AM, DAY 2") == 960
    assert get_minutes_per_race("12:35 AM, DAY 2") == 995
    assert get_minutes_per_race("12:35 PM, DAY 2") == 1715
    with pytest.raises(ValueError):
        get_minutes_per_race("")


def test_average_minutes():
    assert average_minutes([]) == -1
    assert average_minutes(["08:30 AM, DAY 2", "9:30 PM, DAY 10"]) == 7620
    assert average_minutes(["08:30 AM, DAY 2"]) == 1470
    assert average_minutes(["08:00 AM, DAY 1"]) == 0
    assert average_minutes(["08:30 AM, DAY 2", "12:35 AM, DAY 2"]) == 1233
    assert average_minutes(["12:00 PM, DAY 1", "12:01 PM, DAY 1"]) == 241
    assert average_minutes(["12:00 AM, DAY 2"]) == 960
    assert average_minutes(["02:00 PM, DAY 19", "02:00 PM, DAY 20", "01:58 PM, DAY 20"]) == 27239

    # Invalid input
    with pytest.raises(ValueError):
        average_minutes(["08:30 AM, DAY 2", "07:30 AM, DAY 1"])
        average_minutes(["08:30 AM, DAY 2", ""])

