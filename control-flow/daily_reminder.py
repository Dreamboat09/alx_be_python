task = input("Enter your task: ").lower()
priority = input("enter a Priority level (high, medium, low); ").lower()
time_bound = input("Is it time-bound? (yes/no); ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}'is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"'{task}'is a low priority task that requires attention today!")
        else:
            print("is the task time-bound? yes or no answer")

    case "medium":
        if time_bound == "yes":
            print(f"'{task}'is a medium priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"'{task}'is a medium priority task that requires attention")
        else:
            print("is the task time-bound? yes or no answer")

    case "low":
        if time_bound == "yes":
            print(f"'{task}'is a low priority task that requires attention")
        elif time_bound == "no":
            print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("is the task time-bound? yes or no answer")

    case _:
        print("invalid priority level. Please enter high, medium, or low")