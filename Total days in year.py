def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    if year < 1582 or month < 1 or month > 12 or day < 1:
        return None
    
    # Calculate the days from the start of the year up to the month before the given month
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md is None:
            return None
        days += md
    
    # Add the days of the current month
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        days += day
    else:
        return None  # Invalid day

    return days

# Test the function
print(day_of_year(2004, 12, 31))  # Expected output: 366 for a leap year
