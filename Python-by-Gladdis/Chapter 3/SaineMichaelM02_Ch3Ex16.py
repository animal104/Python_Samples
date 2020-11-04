#Mickey "very Diligent" Saine
#SDEV 140
# This program is designed to calculate a mathematical formula to determine how many days were in February of that year.
#13 September 2020



import time

print("Welcome to the February Leap Year Calender Conversion Configuration ...")										#Provides user with Title
print("version 1.0") 																									#Provides Version Number
print ("")
time.sleep(1)
print("This program is designed to input a year and determine whether that year is a leap year or not...")				#Provides User with Lay-man definition of issue 
print ("")	
time.sleep(1)
print ("")
print ("Patent pending, 2020")
print ("")
time.sleep(1)
print ("So let\'s get started with this simple question to warm up, shall we?...")
print ("")
name= input("What is your first and last name:")																		#Shows name on screen, as per Instructor's Requirement
print ("")
print ("Well, ", name, ". That first answer checks out!", sep="")
print ("")
time.sleep(1)

year= int (input("So, Please enter the year that you wish to look up:"))												#take input here

print ("")
time.sleep(1)


if (year % 100) == 0 and (year % 400):																					#determine if the year is divisible by 100 AND that it is also divisible by 400
    print("February ", year, " has 29 days and is a leap year.")
elif (year % 100) != 0 and (year % 4) == 0:																				#determine if the year is NOT divisible by 100 AND that it is also divisible by 4
    print("February ", year, " has 29 days and is a leap year.")
else:
    print("February", year, "has 28 days and is not a leap year.")