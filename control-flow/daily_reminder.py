task = input("input task description")
priority = input("task priority(high, low, medium")
time_bound = input("Is the task time bound(yes/no)")

reminder = ""
        
match priority:
    case "high":
        remeinder = "The task is of high priority"
    case "medium":
        remeinder = "The task is of medium priority"
    case "low":
        reminder = "The task is of low priority"
    case_:
        reminder = "Invalid priority level entered"

if time_bound == "yes":
    remeinder =+ "that requires immediate attention today!"


print(reminder)    

