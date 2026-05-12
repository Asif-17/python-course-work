from datetime import date, time, datetime, timedelta

'''
today = date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())
'''

'''
print(date(2027,6,30))
print(date(2026,2,31))
'''

'''
print(time(23,56,59))
print(time(23,56,59).hour)
print(time(23,56,59).minute)
print(time(23,56,59).second)
'''

'''
now = datetime.now()


print(now)
print("Year: ",now.year)
print("Month: ",now.month)
print("Day: ",now.day)
print("Hour: ",now.hour)
print("Minute: ",now.minute)
print("Second: ",now.second)
'''

'''
now = datetime.now()

print(now.strftime('%d-%m-%Y'))
print(now.strftime('%d/%m/%Y'))
print(now.strftime('%d/%m/%y'))
print(now.strftime('%d/%m/%y %H:%M:%S'))
print(now.strftime('%d/%m/%y %I:%M:%S'))
print(now.strftime('%d/%m/%y %I:%M:%S %p'))
print(now.strftime('%d %m %Y %I:%M:%S %p'))
print(now.strftime('%a %d %b %Y %I:%M:%S %p'))
print(now.strftime('%A %d %B %Y %I:%M:%S %p'))
'''

'''
now = datetime.now()

t_15 = now - timedelta(days=60)
t_16 = now + timedelta(days=60)

print(t_15)
print(t_16)
'''


