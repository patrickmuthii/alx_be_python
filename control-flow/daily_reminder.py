task = str(input("input task description"))
priority = str(input("task priority(high, low, medium"))
time_bound = str(input("Is the task time bound(yes/no)"))

reminder = ""
        
match priority:
    case "high":
        reminder = "The task is of high priority"
    case "medium":
        reminder = "The task is of medium priority"
    case "low":
        reminder = "The task is of low priority"
    case _:
        reminder = "Invalid priority level entered"

if time_bound == "yes":
    reminder += "that requires immediate attention today!i"


print(reminder)    

