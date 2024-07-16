
from datetime import datetime

date_now = datetime.now()
print(type(date_now))
print(date_now)

from datetime import timedelta

date_tomorrow = date_now + timedelta(days=1)

for i in range(4):
    timedelta =+ 1
    print(date_tomorrow)

a_dict = {'my_date' : date_now}
print(type(a_dict['my_date']))
print(a_dict)

print(date_now.strftime("%A"))
print(date_now.strftime("%A %d %B %Y at %H:%M:%S"))
print(date_now.strftime("%A %d %b %y at %H:%M:%S"))
print(date_now.strftime("%A %D %b %y at %H:%M:%S"))
print(date_now.strftime("%a"))

