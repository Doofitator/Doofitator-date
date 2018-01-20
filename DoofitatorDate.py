import calendar
import time
from datetime import datetime

def how_many_days_in_a_month(month, year): #month as MM. year as YYYY.
    if str(month) == '01':
        return 31
    if str(month) == '02':
        if calendar.isleap(int(year)) == True:
            return 29
        else:
            return 28
    if str(month) == '03':
        return 31
    if str(month) == '04':
        return 30
    if str(month) == '05':
        return 31
    if str(month) == '06':
        return 30
    if str(month) == '07':
        return 31
    if str(month) == '08':
        return 31
    if str(month) == '09':
        return 30
    if str(month) == '10':
        return 31
    if str(month) == '11':
        return 30
    if str(month) == '12':
        return 31
    
def the_date_in_x_days(x, since_when): #since_when as YYYY_DD_MM, x as INTEGER.
    utc_datetime = str(datetime.utcnow())
    utc_year = utc_datetime[0:4]
    utc_month = utc_datetime[5:7]
    utc_date = utc_datetime[8:10]
    utc_hour = utc_datetime[11:13]
    utc_minute = utc_datetime[14:16]
    
    since_year = since_when[0:4]
    since_month = since_when[8:10]
    since_day = since_when[5:7]
    
    days_in_current_month = how_many_days_in_a_month(utc_month, utc_year)
    since_plus_x = int(since_day) + x
    next_date = since_plus_x - days_in_current_month
    next_month = int(since_month) + 1
    the_month_after = int(since_month) + 1
    days_in_second_month = how_many_days_in_a_month("%02d" % (int(utc_month)+1,), utc_year)
    if next_date > days_in_second_month:
        next_month = int(since_month) + 2
        next_date = next_date - days_in_second_month
    if next_month == 13:
        year = int(since_year) + 1
        next_month = 1
    else:
        year = since_year
    
    date_in_x_days = str(year) + '_' + str("%02d" % (next_date,)) + '_' + str("%02d" % (next_month,)) #YYYY_DD_MM
    return date_in_x_days
    
    
def time_in_their_timezone(timezone): #timezone as p10 (for utc+10) or m4 (utc-4), etc.
    utc_datetime = str(datetime.utcnow())
    utc_hour = utc_datetime[11:13]
    utc_minute = utc_datetime[14:16]
    
    if 'p' in str(timezone):
        if '.5' in str(timezone):
            the_utc_offset = timezone.lstrip('p')
            the_utc_offset_hour = timezone.lstrip('.5')
            the_utc_offset_minute = '30'
            their_hour = int(utc_hour) + int(the_utc_offset_hour)
            #but what if that makes their hour 25, 32, etc.
            their_minute = int(utc_minute) + int(the_utc_offset_minute)
            #but what if that makes their minute 64, 82, etc.
        else:
            the_utc_offset = timezone.lstrip('p')
            their_hour = int(utc_hour) + int(the_utc_offset)
            #but what if that makes their hour 25, 32, etc.
            their_minute = utc_minute
    elif 'm' in str(timezone):
        if '.5' in str(timezone):
            the_utc_offset = timezone.lstrip('m')
            the_utc_offset_hour = timezone.lstrip('.5')
            the_utc_offset_minute = '30'
            their_hour = int(utc_hour) - int(the_utc_offset_hour)
            #but what if that makes their hour -10, -4, etc.
            their_minute = int(utc_minute) - int(the_utc_offset_minute)
            #but what if that makes their minute -23, -46, etc.
        else:
            the_utc_offset = timezone.lstrip('m')
            their_hour = int(utc_hour) - int(the_utc_offset)
            #but what if that makes their hour -10, -4, etc.
            their_minute = utc_minute
    
    if their_hour > 24:
        their_hour = their_hour - 24

    if their_hour < 0:
        their_hour = 24 + their_hour
    
    return str("%02d" % (their_hour,)) + str(their_minute)
