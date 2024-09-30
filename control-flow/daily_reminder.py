task = input('Enter your task: ')
priority = input('Priority (high/medium/low): ').lower
time_bound = input('Is it time-bound? (yes/no): ').lower
match priority:
    case _ if priority == 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a {time_bound} priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"Note: '{task}' is a {time_bound} priority task. Consider completing it when you have free time.")
        else:
            print('error')
    case _ if priority == 'medium':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a {time_bound} priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"Note: '{task}' is a {time_bound} priority task. Consider completing it when you have free time.")
        else:
            print('error')
    case _ if priority == 'low':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a {time_bound} priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"Note: '{task}' is a {time_bound} priority task. Consider completing it when you have free time.")
        else:
            print('error')
    case _:
        print('error')