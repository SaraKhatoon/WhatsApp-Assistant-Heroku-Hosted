import datetime
from datetime import datetime, timedelta
from calendar import monthrange

def calender_f1():
    date=''
    now = datetime.now()
    date=now.strftime('%H:%M:%S on %A, %B the %dth, %Y')
    print(date)
    return date
def calender_f2():
    presentday = datetime.now()
    tomorrow = presentday + timedelta(1)
    date1=tomorrow.strftime('%A, %B the %dth, %Y')
    print(date1)
    return date1
def calendar_f3(msg):
    year=int(msg[-4:])
    res=''
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                res="{0} is a leap year".format(year)
            else:
                res="{0} is not a leap year".format(year)
        else:
            res="{0} is a leap year".format(year)
    else:
        res="{0} is not a leap year".format(year)
    print(res)
    return res
def calendar_f4(msg):
    segments = msg.split()
    year = int(segments[len(segments) - 1])
    month = int(segments[len(segments) - 2])
    days=''
    days=str(monthrange(year, month)[1]) + " days"
    print(days)
    return days


def calendar_f5(msg):
    ref_year = 2020
    ref_year_islamic = 1441
    year = int(msg[-4:])
    islamic_year = (year - ref_year) + ref_year_islamic
    print(islamic_year)
    if(str(islamic_year))[-1] == '1':
        return str(year) + " is " + str(islamic_year) + "st islamic year"
    if(str(islamic_year))[-1] == '2':
        return str(year) + " is " + str(islamic_year) + "nd islamic year"
    if(str(islamic_year))[-1] == '3':
        return str(year) + " is " + str(islamic_year) + "rd islamic year"
    return str(year) + " is the " + str(islamic_year) + "th islamic year"

