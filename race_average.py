import typing
import sys
import math


def round_average(average: float) -> int:
    if average - int(average) >= .5:
        return math.ceil(average)
    else:
        return math.floor(average)


def parse_date(race_time: str) -> typing.Tuple:
    parsed_date = race_time.split(":")

    # Get hour
    hour = int(parsed_date[0])
    # Get minutes
    parsed_date = parsed_date[1].split(" ")
    minutes = int(parsed_date[0])
    if minutes < 0 or minutes > 59 or hour < 1 or hour > 12:
        raise ValueError("Invalid hour and/or minutes for the following finish time: %s", race_time)
    # Set 12 to hr 0 for calculations
    if hour == 12:
        hour = 0
    # Set AM/PM
    is_am = False
    if parsed_date[1][0] == 'A':
        is_am = True
    # Get day
    day = int(parsed_date[3])

    # Check if end is before start time
    if day == 1 and is_am and hour < 8:
        raise ValueError("Finish time cannot be before start time.")

    return hour, minutes, is_am, day


def get_minutes_per_race(race_time: str) -> int:
    if len(race_time) == 0:
        raise ValueError("Empty string: invalid finish time")
    hour, minutes, is_am, day = parse_date(race_time)
    total_minutes = (day * 24 * 60) - (8 * 60)  # Initialize to full 'd' days minus start time

    # Subtract full end hours from final day
    if is_am:
        total_minutes -= (12*60)

    total_minutes -= ((12 - hour)*60)

    # Add minutes back
    total_minutes += minutes

    return total_minutes


def average_minutes(times:[str]) -> int:
    if len(times) == 0:
        return -1
    sum_times = 0
    for i in range(0, len(times)):
        sum_times += get_minutes_per_race(times[i])
    return round_average((sum_times/len(times)))


def main():
    finish_times = sys.argv[1].split("|")
    print(average_minutes(finish_times))


if __name__ == '__main__':
    main()
