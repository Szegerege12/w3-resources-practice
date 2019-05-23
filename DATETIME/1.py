"""Write a Python script to display the various Date Time formats"""


import datetime
from  datetime import date

print("Current date and time:", datetime.datetime.now())
print("Current year:", datetime.date.today().strftime("%Y"))
print("Month of the year:", datetime.date.today().strftime("%B"))
print("Week number of the year:", datetime.date.today().strftime("%W"))
print("Day of the week:", datetime.date.today().strftime("%w"))
print("Day of year:", datetime.date.today().strftime("%j"))
print("Day of the month:", datetime.date.today().strftime("%d"))


