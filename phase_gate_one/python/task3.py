def days_of_the_week():
    days_in_week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Tursday",
        "Friday",
        "Saturday", 
    ]

    user_today_input = int(input("Enter today's day eg(1 - 7): "))
    elapsed_day_input = int(input("Enter the number of days elapsed since today eg(1 - 7): "))
    
    if user_today_input < 1 or user_today_input > 7:
        print("invalid start day entry in a week should be 1 - 7.")
    elif elapsed_day_input < 1 or elapsed_day_input > 7:
        print("Invalid elapse day in a week.")
    else:
        print(f"Today is {days_in_week[user_today_input]} and the future day is {days_in_week[elapsed_day_input]}")


days_of_the_week()
