# explore_datetime.py

# This script demonstrates handling dates and times using the datetime module.
# It includes functions to display the current date and time, and to calculate a future date.

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format and print the current date and time in "YYYY-MM-DD HH:MM:SS"
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # Get the current date
    current_date = datetime.now()

    # Prompt the user to enter the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))

    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)

    # Print the future date in "YYYY-MM-DD" format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Run the functions to display current datetime and calculate future date
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
