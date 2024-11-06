# Samuel Clackler
# Lab Section: 11
# Submission Date:
# Sources: Chat GPT

Months_and_Days = {
    'Jan':31,
    'Feb':28,
    'leap_Feb':29,
    'Mar':31,
    'Apr':30,
    'May':31,
    'Jun':30,
    'Jul':31,
    'Aug':31,
    'Sep':30,
    'Oct':31,
    'Nov':30,
    'Dec':31
}

Days_of_Week = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]

Input_User = input("Please enter a valid date in mmddyyyy format: ")
# ChatGPT helped with finding leap year 
def leap_year():
    year = int(Input_User[-4:])
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            print("This is a Valid leap year!")
    else:
         print("Please enter a valid Leap year.")

leap_year()
'''
def jan_start():

def valid_date():

def day_of_week():
'''