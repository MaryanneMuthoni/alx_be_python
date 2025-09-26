# create a Python script named explore_datetime.py. 
# This script will demonstrate your ability to use the datetime module

from datetime import date, time, datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date 

def calculate_future_date():
    print("Current date and time:", display_current_datetime().strftime("%Y-%m-%d %H:%M:%S"))
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = display_current_datetime() + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    calculate_future_date()
