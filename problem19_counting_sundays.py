year = 1900
day = 1 # day of the month
month = 1 # Jan, Feb, etc.
dow = 0 # day of the week is indexed at zero for easier modular arithmetic
# 1 = Monday, ... , 7 = Sunday
days_in_months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

sunday_count = 0
while year <= 2000:
    # check if today is sunday 

    if year % 4 == 0 and year != 1900 and month == 2:
        month += 1
        dow += 29
        dow = dow % 7
    else:
        # it's not a leap month
        dow += days_in_months[month] 
        dow = dow % 7
        if month == 12:
            month = 1
            year += 1
        else: month += 1

    if dow == 6 and year > 1900: sunday_count += 1

print(sunday_count)
