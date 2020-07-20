# Step 1
import time
import winsound
from time import sleep

# Step 2
def sleep_days(days):
    sleep(days * 86400)

def sleep_weeks(weeks):
    sleep(weeks * 604800)

def sleep_years(years):
    sleep(years * 31536000)

def sleep_months(months):
    sleep(months * 2628000)

def sleep_leap_years(leap_years):
    sleep(leap_years * 31622400 )
    
def sleep_minutes(minutes):
    sleep(minutes * 60)

def sleep_hours(hours):
    sleep(hours * 3600)

# Step 3
a = int(input("Enter how many times I have beep when i'm done  > "))
b = int(input("Enter when to beep (in Years) > "))
c = int(input("Enter when to beep (in Leap Years) > "))
d = int(input("Enter when to beep (in Months) > "))
e = int(input("Enter when to beep (in Weeks) > "))
f = int(input("Enter when to beep (in Days) > "))
g = int(input("Enter when to beep (in Hours) > "))
h = int(input("Enter when to beep (in Minutes) > "))
i = int(input("Enter when to beep (in Seconds) > "))

# Step 4
sleep_years(b)
sleep_leap_years(c)
sleep_months(d)
sleep_weeks(e)
sleep_days(f)
sleep_hours(g)
sleep_minutes(h)
time.sleep(i)

# Step 5
for i in range(a):
    winsound.Beep(3000,100)
    winsound.Beep(2500,100)
    winsound.Beep(2000,100)    
    winsound.Beep(1000,100)    
    winsound.Beep(500,100)
    winsound.Beep(2000,100)
    winsound.Beep(800, 90)

# Step 6
print('DONE')