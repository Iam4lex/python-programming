

import datetime
from datetime import datetime
from datetime import date

print(dir(datetime))

# ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']  

now = datetime.now()

print(now) # 2024-09-24 21:32:23.481822

year = now.year
month = now.month
day = now.day
hour = now.hour
second = now.second
timestamp = now.timestamp()

print(year) # 2024
print(month) # 9
print(day)
print(hour)
print(second)
print(timestamp)

today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00