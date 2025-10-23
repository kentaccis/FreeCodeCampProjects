def add_time(start, duration, day=None):
    # split start time
    time_part, am_pm = start.split()
    hour, minute = map(int, time_part.split(":"))
    duration_hour, duration_minute = map(int, duration.split(":"))

    # convert start hour to 24-hour format
    if am_pm.upper() == "PM" and hour != 12:
        hour += 12
    elif am_pm.upper() == "AM" and hour == 12:
        hour = 0

    # add duration
    total_minutes = minute + duration_minute
    extra_hours, new_minute = divmod(total_minutes, 60)
    total_hours = hour + duration_hour + extra_hours

    # count full days passed
    days_passed = total_hours // 24
    remaining_hours = total_hours % 24

    # convert back to 12-hour format with AM/PM
    if remaining_hours == 0:
        display_hour = 12
        new_am_pm = "AM"
    elif remaining_hours < 12:
        display_hour = remaining_hours
        new_am_pm = "AM"
    elif remaining_hours == 12:
        display_hour = 12
        new_am_pm = "PM"
    else:
        display_hour = remaining_hours - 12
        new_am_pm = "PM"

    # handle day of the week if provided
    if day:
        days_list = ["Monday", "Tuesday", "Wednesday",
                     "Thursday", "Friday", "Saturday", "Sunday"]
        new_day_index = (days_list.index(day.capitalize()) + days_passed) % 7
        new_day = days_list[new_day_index]

    # build final time string
    new_time = f"{display_hour}:{new_minute:02d} {new_am_pm}"
    if day:
        new_time += f", {new_day}"
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time
