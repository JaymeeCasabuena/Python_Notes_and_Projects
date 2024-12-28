"""
Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

"""

def add_time(start, duration, day=''):

    days_in_a_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    # Parse input
    time, am_pm = start.split()
    start_hours, start_mins = map(int, time.split(':'))
    duration_hours, duration_mins = map(int, duration.split(':'))

    # Calculate new time
    new_time_mins = start_mins + duration_mins
    new_time_hours = start_hours + duration_hours + new_time_mins // 60
    new_time_mins %= 60

    # Determine AM/PM and flips
    flips = new_time_hours // 12
    new_time_hours %= 12
    if new_time_hours == 0:
        new_time_hours = 12

    if flips % 2 == 1:
        am_pm = 'AM' if am_pm == 'PM' else 'PM'

    # Calculate total days
    print(am_pm, "HI")
    total_days = (start_hours + duration_hours + (start_mins + duration_mins) // 60) // 24
    if am_pm == 'AM' and flips % 2 == 1:
        total_days += 1

    # Determine day of the week
    if day:
        day = day.capitalize()
        day_index = (days_in_a_week.index(day) + total_days) % len(days_in_a_week)
        formatted_day = days_in_a_week[day_index]
    else:
        formatted_day = ''

    # Format "later" text
    if total_days > 1:
        later = f' ({total_days} days later)'
    elif total_days == 1:
        later = ' (next day)'
    else:
        later = ''

    # Return formatted result
    return f'{new_time_hours}:{new_time_mins:02d} {am_pm}{f", {formatted_day}" if formatted_day else ""}{later}'


