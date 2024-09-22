# Prompt user for task details
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes or no): ").lower()

# Generate the reminder message based on priority using match case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' is an unkwown priority task."

# Add time-sensitivity condition
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += "Consider completing it when you have free time."

# Display the customized reminder
print(reminder)
