#Mickey "going to job" Saine
#SDEV 220
#Write a program that displays the area and perimeter of a Hexagon  
#06 September 2020

import time
import math


print("Welcome to the Contraption of Hexagonian Magic")																									#Defining the project for the user
print("version 1.0") 																																	#Provides Version Number
print ("")
time.sleep(1)
print("This program understand, calculate and possible pontificate on the very area and the perimeter a Hexagon!")										#Define the purpose to the User
print ("Patent pending, 2020")
print ("")
time.sleep(1)

side=float(input("Question 1: So, What is the Width, in inches, of one of the sides of this Hexagon that you're referring to:"))						#Receive user input for unknown variables

area = ((3 * math.sqrt(3) * (side * side)) / 2)																											#Calculate area


perimeter = (side * 6)																																	#Calculate Side

print("The Area of a Hexagon, based on the measure that was provided is", area, "inches, and the perimeter is equal to", perimeter, "inches.")			#Provide Output. I choose not to use any round functions because of the geometry factor, for other uses