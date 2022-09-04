from math import floor


hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

# get the hours + minutes of the minutes input
minutes = (dura + mins) % 60
hours = floor((dura + mins) / 60)
hours = (hours+hour) % 24
print(hours, ":", minutes,sep="")