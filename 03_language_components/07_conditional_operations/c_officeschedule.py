#!/usr/bin/python3
"""
Purpose: Office Schedule
    Monday to Friday  :- 9 am CDT to 5 pm CDT
    Saturday          :- 9 am CDT to 1 pm CDT
    Sunday            :- Holiday

   
"""

# week_of_day = "Monday"
week_of_day = input("Enter week of the day:").strip().title()

# Method 1 -  MEMBERSHIP CHECK
WEEKDAY_TIMINGS = "TIMINGS: 9 AM to 6 PM"
if  week_of_day in ("Monday" , "Tuesday" , "Wednesday", "Thursday" or  
    week_of_day == "Friday"
    ):
    print(WEEKDAY_TIMINGS)
elif week_of_day == "Saturday": # or week_of_day == "saturday":
    print("TIMINGS: 9 AM to 1 PM")
elif week_of_day == "Sunday":
    print("----HOLIDAY----------")
else:
    print("INVALID ENTRY! PLEASE TRY AGAIN!!")
