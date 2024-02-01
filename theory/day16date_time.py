### Date Time ###
#   provides classes for working with dates and times. 

# 1 - Getting datetime Information

from datetime import datetime, time, date
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

# 2 - Formatting Date Output Using strftime
# Import the datetime module to work with dates and times

# Define a function to format the current date and time
def format_current_datetime():
    # Get the current date and time
    current_datetime = datetime.now()

    # Format the date and time into a string using strftime
    formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Return the formatted date and time
    return formatted_date

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the format_current_datetime function to get the formatted date and time
    formatted_datetime = format_current_datetime()

    # Print the formatted date and time
    print("Current Date and Time:", formatted_datetime)
# 3 - String to Time Using strptime
date_string = "2022-01-01 12:30:00"

parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# 4 - Using date from datetime

# Create a datetime object representing a specific date and time
datetime_obj = datetime(2022, 1, 1, 12, 30, 0)

# Use the date() method to extract the date part
date_only = datetime_obj.date()

# Print the result
print("Original Datetime:", datetime_obj)
print("Date Only:", date_only)
# 5 - Time Objects to Represent Time

# Create a datetime object representing a specific date and time
datetime_obj = datetime(2022, 1, 1, 12, 30, 0)

# Use the time() method to extract the time part
time_only = datetime_obj.time()

# Print the result
print("Original Datetime:", datetime_obj)
print("Time Only:", time_only)


# Create a time object representing a specific time
time_obj = time(12, 30, 0)

# Print the result
print("Time Only:", time_obj)
# 6 - Difference Between Two Points in Time Using
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00
# 7 - Difference Between Two Points in Time Using timedelta
start_time = datetime(2022, 1, 1, 12, 0, 0)
end_time = datetime(2022, 1, 1, 14, 30, 0)

# Calculate the time difference between the two datetime objects
time_difference = end_time - start_time

# Convert the time difference to hours, minutes, and seconds
hours, remainder = divmod(time_difference.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# Print the result
print("Start Time:", start_time)
print("End Time:", end_time)
print("Time Difference:", time_difference)
print("Time Difference (Formatted): {} hours, {} minutes, {} seconds".format(hours, minutes, seconds))