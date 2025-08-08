from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))

day = input("Enter the number of days to add to the current date: ")

def calculate_future_date():
    future_date = datetime.now() + timedelta(days=int(day))
    print(f"Future date: {future_date.strftime("%Y-%m-%d %H:%M:%S")}")