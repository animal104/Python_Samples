#Mickey "likes fittos" Saine
#SDEV 140
# A program to let the user enter a non negative integer loop to calculate the factorial of a number
#20 September 2020



import time

print("Welcome to the Children's Mathematical Nonnegative Integer factor able calculator...")								#Provides user with Title
print("version 1.0") 																										#Provides Version Number
print ("")
time.sleep(1)
print("This program is designed to take a non-negative integer and calculate the factorial for the number...")				#Provides User with Lay-man definition of issue 
print ("")
time.sleep(1)
print ("")
print ("Patent pending, 2020")
print ("")
time.sleep(1)
print ("So let\'s get started with this simple question that we will match with the computer\'s answer...")
print ('')
name= input("What is your first and last name to ensure it's on this form for credit:")										#Shows name on screen, as per Instructor's Requirement
print ("")
print ("Well, ", name, ". That first answer checks out!", sep="")

number= int(input("So, what number can I calculate the Factorial for you? <Please make sure it's a positive number:"))	

factorial = 1


if number < 0:																													# check if the number is negative, positive or zero
   print("Sorry, factorial does not exist for negative numbers")																#exit statement if the number is invalid
elif number == 0:																												#else statement to print factorial for 0, because it doesn't apply to the formula
   print("The factorial of 0 is 1")
else:
   for i in range(1,number + 1):																								#nested if statement to run number through factorial formula
       factorial = factorial*i
   print("The answer to the factorial of",number,"is",factorial, ". Aren't you glad we discussed this now ^_^.")																				