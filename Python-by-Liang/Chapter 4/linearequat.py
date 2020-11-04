#Mickey "trys hard to be functional and elegant" Saine
#SDEV 220
#Write a program that uses Cramer’s rule to solve the following 2 × 2 system of linear equation: 
#06 September 2020

import time
import math

print("Welcome to an algebraical discussion of Dr. Cramer\'s rule of solving 2 x 2 systems of linear equations...")												#Defining the project for the user
print("version 1.0") 																																			#Provides Version Number
print ("")
time.sleep(1)
print("What is this program designed to do?")
print ("")
time.sleep(1)
print("To be honest, I don't much understand after four hours of YouTubing that level of Math.")																#Should Define the purpose to the User, but I don't get the math. 
print ("")																																						#It just follows the listed formulas and hopes for the best.
print("I just know it does something that the instructions told me to make it do!")
print ("")
print ("Patent pending, 2020")
print ("")
time.sleep(1)
print ("So let\'s get started on this equation, defining some values")


a=float(input("Please Define a value for A:"))																													#Gets the appropriate variables for solving the equation
b=float(input("Please Define a value for B:"))
c=float(input("Please Define a value for C:"))
d=float(input("Please Define a value for D:"))
e=float(input("Please Define a value for E:"))
f=float(input("Please Define a value for F:"))

x = (e*d-b*f)/(a*d-b*c)																																			#equation that the variables work through to determine the answer 
y = (a*f-e*d)/(a*d-b*c)

e=a*x + b*y
f=c*x + d*y

print ("")
time.sleep(1)

if x-y == 0:																																					#Evaluation on whether the chosen variables fit the theory
		print("Those work! You choose the following variables: \"", a, ", " ,b, ", ", c, ", ", d, ", ", e, ", and ", f, "\" as your choices.", sep='')
else:
		print("These numbers do not work with this equation. Have you thought about using another system to evaluate?")