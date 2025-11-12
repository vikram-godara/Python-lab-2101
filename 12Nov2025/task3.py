import datetime


# Function to get day of the week from a date string
def get_day_of_week(date_string):
    """
    Takes a date string in YYYY-MM-DD format
    Returns the day of the week
    """
    try:
        # Convert string to datetime object
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')

        # Get day of the week
        day = date_obj.strftime('%A')

        return day

    except ValueError:
        return "Invalid date format! Please use YYYY-MM-DD"


# Test the function with various dates
print("Testing get_day_of_week function:\n")
print("-" * 40)

# Test 1
date1 = "2024-01-01"
print(f"{date1} was a {get_day_of_week(date1)}")

# Test 2
date2 = "2025-11-12"
print(f"{date2} is a {get_day_of_week(date2)}")

# Test 3
date3 = "2000-01-01"
print(f"{date3} was a {get_day_of_week(date3)}")

# Test 4
date4 = "1995-08-15"
print(f"{date4} was a {get_day_of_week(date4)}")

# Test 5
date5 = "2030-12-25"
print(f"{date5} will be a {get_day_of_week(date5)}")

print("-" * 40)

# Test with invalid format
print("\nTesting with invalid format:")
date6 = "12-11-2024"
print(f"{date6}: {get_day_of_week(date6)}")