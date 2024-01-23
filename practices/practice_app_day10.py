# One Day Schedule App (Complex Version)

schedule = {}
time_slots = ["morning", "afternoon", "evening", "night"]
for slot in time_slots:
    print(f"What are your plans for {slot}?")
    activities = input("Enter activities separated by commas: ")
    durations = input("Enter corresponding durations (in minutes) separated by commas: ")

    activities_list = activities.split(',')
    durations_list = [int(duration) for duration in durations.split(',')]

    schedule[slot] = {"activities": activities_list, "durations": durations_list}
total_time = 0
print("\nYour Detailed Schedule for the Day:")
for slot, data in schedule.items():
    activities = data["activities"]
    durations = data["durations"]

    print(f"{slot.capitalize()}:")
    for i, activity in enumerate(activities):
        print(f"  {activity} - Duration: {durations[i]} minutes")
        total_time += durations[i]
print("\nTotal Time Spent: {} minutes".format(total_time))