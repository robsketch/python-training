from math import floor

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

# get the hours + minutes of the minutes input
minutes = (dura + mins) % 60
hours = floor((dura + mins) / 60)
hours = (hours+hour) % 24
print(hours,":", minutes,sep="")

##############################################################################

# LAB description:

# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

# Don't worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data.

# Test your code carefully. Hint: using the % operator may be the key to success.

# Test Data
# Sample input:
# 12
# 17
# 59

# Expected output: 13:16


# Sample input:
# 23
# 58
# 642

# Expected output: 10:40


# Sample input:
# 0
# 1
# 2939

# Expected output: 1:0

