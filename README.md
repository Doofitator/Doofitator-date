# Doofitator-date
#### A python module for date and time calculations

### Usage:
This module can calculate timezones, the amount of days in a month and the date in a set number of days. There are some known bugs which are referenced further down, however for the most part, use the following.

To calculate the date in a specific number of days, use `the_date_in_x_days(x, since_when)`.
Example:
```python
>>> from DoofitatorDate import the_date_in_x_days
>>> the_date_in_x_days(46, "2018-23-10")
'2018_10_12'
```

To calculate how many days are in a month (including leap year Feburary), use `how_many_days_in_a_month(month, year)`. Note that January is month '01', and December is month '12'.
Example:
```python
>>> from DoofitatorDate import how_many_days_in_a_month
>>> how_many_days_in_a_month('02', 2020)
29
>>> how_many_days_in_a_month('02', 2021)
28
```

Finally, to calculate the time in another timezone, use `time_in_their_timezone(timezone)`. Note that `timezone` is a string: 'p10' is utc+10, or 'm4' is utc-4.
Example:
```python
>>> from DoofitatorDate import time_in_their_timezone
>>> time_in_their_timezone('p4')
'0433' # 33 past 4 in the morning
>>> time_in_their_timezone('p15')
'1533' # 33 past 3 in the afternoon
```

### Bugs

1. ~~There seems to be an issue at certain times with minus timezones showing up as, for example, '-403', instead of '2003' (for 3 past 8 at night)~~
2. There is an issue with the date calculations where dates that do not go over to the next month cause an issue. For example, `>>> the_date_in_x_days(2, "2018-20-01")` returns the technically correct answer of `'2018_-9_02'`, however it really should return `'2018_22_01'`.
