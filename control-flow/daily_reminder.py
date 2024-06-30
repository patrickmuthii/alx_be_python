Task = str(input("Enter the task description"))
Priority = str(input("Enter the task's priority(high, low, medium"))
Time_Bound = str(input("Is the task time-bound(yes or no)"))

reminder = ""
        
match Priority:
    case "high":
        reminder = "The task is of high priority"
    case "medium":
        reminder = "The task is of medium priority"
    case "low":
        reminder = "The task is of low priority"
    case _:
        reminder = "Invalid priority level entered"

if Time_Bound == "yes":
    reminder += "that requires immediate attention today!i"


print(reminder)    

