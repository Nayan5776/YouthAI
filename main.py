import sys
from youthai.tracker import YouthAITracker

def display_menu():
    print("\n" + "=" * 40)
    print("      YOUTH AI - VERSION 0.1")
    print("=" * 40)
    print("1. View/Setup Profile")
    print("2. Daily Goals")
    print("3. Task Manager")
    print("4. Study Hours Tracker")
    print("5. Exit")
    print("=" * 40)

def main():
    tracker = YouthAITracker()

    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            print("\n--- USER PROFILE ---")
            if tracker.profile:
                print(f"Name: {tracker.profile.name}")
                print(f"Age: {tracker.profile.age}")
                print(f"Major/Grade: {tracker.profile.major_or_grade}")
                print(f"Career Goal: {tracker.profile.career_goal}")
            else:
                print("No profile found. Let's create one!")
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                major = input("Enter your Major or Grade: ")
                goal = input("Enter your main career goal: ")
                tracker.set_profile(name, age, major, goal)
                print("Profile saved successfully!")

        elif choice == "2":
            print("\n--- DAILY GOALS ---")
            print("1. View Goals")
            print("2. Add Goal")
            print("3. Complete Goal")
            sub_choice = input("Choose an option: ").strip()

            if sub_choice == "1":
                if not tracker.goals:
                    print("No goals set yet.")
                for idx, g in enumerate(tracker.goals, start=1):
                    status = "✓" if g.is_completed else "✗"
                    print(f"{idx}. [{status}] {g.title}")
            elif sub_choice == "2":
                title = input("Enter goal title: ")
                tracker.add_goal(title)
                print("Goal added!")
            elif sub_choice == "3":
                idx = int(input("Enter goal number to complete: ")) - 1
                if tracker.complete_goal(idx):
                    print("Goal marked as completed!")
                else:
                    print("Invalid goal number.")

        elif choice == "3":
            print("\n--- TASK MANAGER ---")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Complete Task")
            sub_choice = input("Choose an option: ").strip()

            if sub_choice == "1":
                if not tracker.tasks:
                    print("No tasks found.")
                for idx, t in enumerate(tracker.tasks, start=1):
                    status = "✓" if t.is_completed else "✗"
                    print(f"{idx}. [{status}] ({t.priority}) {t.title}")
            elif sub_choice == "2":
                title = input("Enter task description: ")
                priority = input("Priority (High/Medium/Low) [Medium]: ").capitalize() or "Medium"
                tracker.add_task(title, priority)
                print("Task added!")
            elif sub_choice == "3":
                idx = int(input("Enter task number to complete: ")) - 1
                if tracker.complete_task(idx):
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")

        elif choice == "4":
            print("\n--- STUDY HOURS TRACKER ---")
            print("1. Log Study Session")
            print("2. View Total Study Time")
            sub_choice = input("Choose an option: ").strip()

            if sub_choice == "1":
                subject = input("Enter subject name: ")
                minutes = int(input("Enter time spent (in minutes): "))
                tracker.log_study_session(subject, minutes)
                print("Session logged!")
            elif sub_choice == "2":
                total_mins = tracker.get_total_study_minutes()
                hours = total_mins // 60
                mins = total_mins % 60
                print(f"Total Study Time: {hours} hours and {mins} minutes ({total_mins} total minutes)")

        elif choice == "5":
            print("\nGoodbye!")
            sys.exit()
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()