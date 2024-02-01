### Exercices ###
from datetime import datetime, timedelta
# 1 - Get the current day, month, year, hour, minute and timestamp from datetime module
current_datetime = datetime.now()
current_day = current_datetime.day
current_month = current_datetime.month
current_year = current_datetime.year
current_hour = current_datetime.hour
current_minute = current_datetime.minute
current_timestamp = current_datetime.timestamp()
# 2 - Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_current_date = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")
# 3  - Today is 5 December, 2019. Change this time string to time.
time_string = "5 December, 2019"
time_object = datetime.strptime(time_string, "%d %B, %Y").time()
print("Converted Time String to Time:", time_object)
# 4 - Calculate the time difference between now and new year.
new_year = datetime(current_year + 1, 1, 1, 0, 0, 0)
time_until_new_year = new_year - current_datetime
print("Time Difference Until New Year:", time_until_new_year)
# 5 - Calculate the time difference between 1 January 1970 and now.
epoch_time = datetime(1970, 1, 1, 0, 0, 0)
time_since_epoch = current_datetime - epoch_time
print("Time Difference Since Epoch (1970):", time_since_epoch)
'''
6 - Think, what can you use the datetime module for? Examples:
        - Time series analysis
        - To get a timestamp of any activities in an application
        - Adding posts on a blog
'''
# Time series analysis : useful in finance, economics, and various scientific disciplines where time plays a crucial role in the data analysis process.
# Timestamp : logging, tracking user activity, measuring performance, and debugging.
# Adding posts on a blog: It helps in sorting posts chronologically, scheduling future posts, and calculating the time since a post was published.