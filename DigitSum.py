# Python program to compute sum of digits in number.
# Function to get sum of digits


def getSum(n):
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum
n = int(input("Enter a number: "))
print(getSum(n))
'''
# Python program to check if year is a leap year or not
# To get year (integer input) from the user
#bash: line 1: y: command not found
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))
'''
