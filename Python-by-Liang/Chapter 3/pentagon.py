#Mickey "very Diligent" Saine
#SDEV 220
#Write a program that displays the area and the Length of one side of a Pentagon
#06 September 2020

import time
import math

print("Welcome to analysis of Pentagonian Secrecy that has been shrouding for hundreds of years.")																		#Defining the project for the user
print("version 1.0") 																																					#Provides Version Number
print ("")
time.sleep(1)
print("This program is designed to calculate little Pentagons in order to find the turth about the largest Pentagon out there!!")										#Define the purpose to the User
print ("Patent pending, 2020")
print ("")
time.sleep(1)

radius=float(input("Question 1: So, What is the number, in inches, of the length from the center of a pentagon to a vertex:"))											#receive input from user to get radius

side_Length = 2*radius*math.sin(math.pi/5)																																#formula to calculate the Side Length

area = side_Length **2*((3 * math.sqrt(3)) / 2)																															#formula to calculate the area 

print("The Area of a Pentagon, based on the measure that was provided is", area, "inches, and this means a side length would be equal to", side_Length, "inches.")		#Final output with requested information