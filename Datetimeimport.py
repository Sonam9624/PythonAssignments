
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta


#create date, time , datetime object
now=datetime.now()
print(now)

print("----------------------------")

d=date(2020,5,21)
print("Date:",d)

print("----------------------------")

t=time(11,15,0)
print("Time: ",t)

print("----------------------------")

dt=datetime(2025,5,20,11,15,0)
print(dt)

print("----------------------------")

print('year', now.strftime("%Y"))
print('month name',now.strftime("%B"))
print('day of week', now.strftime("%A"))

print("----------------------------")

#parse string to datetime object

dt_str='20-05-2025 14:20:15'


 #convert str to datetime
 
dt_obj=datetime.strptime(dt_str, "%d-%m-%Y %H:%M:%S")
print(dt_obj)


print("----------------------------")

today=date.today()
print("Today :", today)

print("----------------------------")

tomorrow=today + timedelta(days=1)
yes=today- timedelta(days=1)

print('tomorrow ',tomorrow)
print('yesterday ',yes)


print("----------------------------")


from datetime import datetime
import pytz

utc=pytz.utc
print(utc)

ist=pytz.timezone('Asia/Kolkata')
print(ist)

utc_now = datetime.now(utc)

print(utc_now)

ist_now=utc_now.astimezone(ist)

print(ist_now)
