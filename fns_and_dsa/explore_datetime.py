from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date)
    
display_current_datetime("%Y-%m-%d %H:%M:%S")
    
def calculate_future_date():
    number_of_days = int(input('enter a number of days: '))
    current_date = date.today()
    future_date = current_date + timedelta(days=number_of_days)
    print(future_date)
    
calculate_future_date()