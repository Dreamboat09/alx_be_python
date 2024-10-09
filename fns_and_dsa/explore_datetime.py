from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date)
    
display_current_datetime("%Y-%m-%d %H:%M:%S")
    
def calculate_future_date():
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    current_date = date.today()
    future_date = current_date + timedelta(days=number_of_days)
    future_date = future_date.strftime
    print(future_date)
    
calculate_future_date("%Y-%m-%d %H:%M:%S")