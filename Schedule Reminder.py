# Schedule Reminder System
import time
from datetime import datetime

reminders = []

while True:
    print("\n--- Schedule Reminder System ---")
    print("Current Time:", datetime.now().strftime("%Y-%m-%d %I:%M%p"))
    print("1. Add Reminder")
    print("2. View Reminders")
    print("3. Delete Reminder")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        date = input("Enter reminder date (YYYY-MM-DD): ")
        target_time = input("Enter target time (HH:MM AM/PM): ").upper()
        task = input("Enter reminder: ")
        current_time = datetime.now().strftime("%Y-%m-%d %I:%M%p")
        reminders.append({
            "date": date,
            "target_time": target_time,
            "task": task,
            "added_time": current_time
        })
        print(f"✅ Reminder added! (Created at {current_time})")
        time.sleep(1)

    elif choice == "2":
        if not reminders:
            print("You don't have any reminders.")
        else:
            print("\nYour Reminders:")
            now = datetime.now()
            for i, r in enumerate(reminders, 1):
                try:

                    reminder_datetime = datetime.strptime(f"{r['date']} {r['target_time']}", "%Y-%m-%d %I:%M%p")
                    if now > reminder_datetime:
                        status = "⏰ Passed"
                    else:
                        status = "🕰️ Upcoming"
                except ValueError:
                    status = "⚠️ Invalid Date/Time Format"

                print(f"{i}. [{r['date']} - {r['target_time']}] {r['task']} ({status}) Added: {r['added_time']}")
        time.sleep(2)

    elif choice == "3":
        if not reminders:
            print("No reminders to delete.")
        else:
            num = int(input("Enter reminder number to delete: "))
            if 0 < num <= len(reminders):
                removed = reminders.pop(num - 1)
                print(f"🗑️ Removed: {removed['task']}")
            else:
                print("Invalid number.")
        time.sleep(1)

    elif choice == "4":
        print("👋 Goodbye! Have a nice day!")
        time.sleep(1)
        break

    else:
        print("Invalid choice. Try again.")
        time.sleep(1)   