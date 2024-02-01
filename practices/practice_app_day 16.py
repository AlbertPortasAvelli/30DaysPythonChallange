from datetime import datetime, timedelta

# Dictionary to store scheduled events with timestamps
events = []

def schedule_event():
    event_description = input("Enter event description: ")
    event_date_str = input("Enter event date (YYYY-MM-DD): ")
    event_time_str = input("Enter event time (HH:MM): ")

    event_datetime_str = f"{event_date_str} {event_time_str}"
    event_datetime = datetime.strptime(event_datetime_str, "%Y-%m-%d %H:%M")

    events.append({"description": event_description, "datetime": event_datetime})
    print("Event scheduled successfully!")

def view_events():
    print("\nScheduled Events:")
    for i, event in enumerate(events, 1):
        event_description = event["description"]
        event_datetime = event["datetime"]
        time_until_event = event_datetime - datetime.now()

        print(f"{i}. {event_description} (Scheduled: {event_datetime}, Time Until: {time_until_event})")

# Application loop
while True:
    print("\nEvent Scheduler Menu:")
    print("1. Schedule Event")
    print("2. View Events")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        schedule_event()
    elif choice == '2':
        view_events()
    elif choice == '3':
        print("Exiting Event Scheduler. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
