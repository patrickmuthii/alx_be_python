task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): ")).lower()
time_bound = str(input("Is it time-bound (yes/no): ")).lower()

reminder = ""
        
match priority:
    case "high":
        reminder = f"The task '{task}' is of high priority"
    case "medium":
        reminder = f"The task '{task}' is of medium priority"
    case "low":
        reminder = f"The task '{task}' is of low priority"
    case _:
        reminder = "Invalid priority level entered"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"


print(reminder)    

