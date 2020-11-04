#Mickey "getting up and getting coffee" Saine
#SDEV 140
#Write a program that asks the users how many cookies (s)he wants to make, then displays the number of cups of each ingredient needed for the specified cookies. 
#06 September 2020

import time
import math

#1 cup = 48 teaspoons

#The following was determined 	-1.5 cups = 72 Teaspoons (Sugar)
#				1 cup = 48 teaspoons (Butter)
#				2.75 cups = 132 teaspoons (flour)
#Therefore			72/48 = 1.5 teaspoons of suger were needed per cookie
#				48/48 = 1 teaspoons of butter were needed per cookie
#				132/42 = 3.14 teaspoons of flour were needed per cookie


print("Welcome to the Cookie Cutter Corundum Exploration.")									#Provides user with Title
print("version 1.0") 																		#Provides Version Number
print ("")
time.sleep(1)
print("This program is designed to take information about the cookies you want, and tell you how much ingredients you need...")		#explains in short hand what is going on
print("From a guy who can't cook Mac N Cheese")
print ("")
print ("Patent pending, 2020")	
print ("")
time.sleep(1)

print ("So let\'s get started with this simple question that we will match with the computer's answer...")
print ("")
name= input("What is your first and last name to ensure it's on this form for credit:")		#Shows name on screen, as per Instructor's Requirement
print ("")
print ("Well ", name, "....", sep='')
cookies= int(input("How many cookies do you want to make:"))								#Define Variable

teaspoons_Of_Sugar = cookies * 1.5
teaspoons_Of_Butter= cookies 
teaspoons_Of_Flour= cookies * 3.14

cups_Of_Sugar = math.ceil(teaspoons_Of_Sugar / 48)											#Converts the Teaspoons back into cups. 
cups_Of_Butter = math.ceil(teaspoons_Of_Butter / 48)										#The round function was invoked, because round number should be close enough for a recipe and easier to understand for the user. math.ceil was 
cups_Of_Flour = math.ceil(teaspoons_Of_Flour / 48)											#chosen because I can't have zero cups, but who knows.! I can't bake!


print("")
print ("")
print ("")
time.sleep(1)
print ("Calculating the amount of cookies...")
print ("")
print ("")
time.sleep(1)
print ("Baking a TINY batch of cookies in your computer to ensure I've got this right...!")
print ("")
print ("")
time.sleep(1)
print ("Eureka, I GOT IT!!")
print ("")
print ("")
print ( "After some careful consideration, it was decided that you need", cups_Of_Sugar, "Cups of Sugar. Next, you will need", cups_Of_Butter, "Cups of Butter. Finally, You will need", cups_Of_Flour, "cups to complete this amount of cookies.")
																							#Final Output
print ("")
print ("")
time.sleep(1)
print ("Good Luck on those cookies! Enjoy!")   
