#  Create a simplified Python script that uses conditional statements,
#+ Match Case, and loops to remind the user about a single, priority task 
#+ for the day based on time sensitivity

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print("Reminder: {task} is a high priority task, do it immediately after the time bound tasks.")
    case 'medium':
        if time_bound == 'yes':
            print(f"{task} is a medium priority task. Start doing it before the deadline.")
        else:
            print(f"{task} is a medium priority task. Do it when you can.")
    case 'low':
        if time_bound == 'yes':
            print(f"Note: {task} is a low priority task. Keep doing it slowly when you have time.")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
