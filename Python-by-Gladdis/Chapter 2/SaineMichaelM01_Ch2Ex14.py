#Mickey "going to job" Saine
#SDEV 140
# This program is designed to determine Compound Interest Savings
#06 September 2020

import time
import math

print("Welcome to the Compound Interest Calculation Contraption...")									#Provides user with Title
print("version 1.0") 																					#Provides Version Number
print ("")
time.sleep(1)
print("This program is designed to determine how much money you will have from compound interest, after saving for a period of time...")
print("This complex program will help save you several lines of excel...")
print ("")
print ("Patent pending, 2020")
print ("")
time.sleep(1)
print ("So let\'s get started with this simple question that we will match with the computer's answer...")


name= input("What is your first and last name to ensure it's on this form for credit:")					#Shows name on screen, as per Instructor's Requirement
print ("")
print ("Well, ", name, ", I have some key questions so we can figure this out!", sep="")
print ("")

principle = float(input("Enter the amount of money that you are starting out with:"))					#Define Variable
print ("Wow, nice start to your savings")
print ("")
annual_Interest_Rate = float(input("Enter the annual interest rate:"))									#Define Variable
print ("That is definitely a good savings rate!")
calculated_Annual_Interest_Rate= annual_Interest_Rate / 100												#convert "Street talk" into a variable fraction
print ("")
number_Of_Compounds = float(input("the number of times (per year) that the interest is compounded:"))	#Define Variable
print ("Great! That's a good number of years to start with!")
print ("")
years = float(input("Enter the number of years the account will be left to earn interest:"))			#Define Variable
print ("I'm very impressed at your commitment to save!")
print ("")


amount_Of_Money = principle * (((1 + (number_Of_Compounds/calculated_Annual_Interest_Rate)) ** (calculated_Annual_Interest_Rate*years)))		#define the Amount of Money

expressed_Amount_Of_Money= "${:,.2f}".format(amount_Of_Money)
expressed_Principle= "${:,.2f}".format(principle)

print ("")
print ("")
time.sleep(1)
print ("Calculating the additional money to be made from your Compound Interest...")
print ("")
print ("")
time.sleep(1)
print ("Working on adding all of those components together!")
print ("")
print ("")
time.sleep(1)
print ("Well, I'm proud to announce a bright future if you maintain this path!!")

print ("You started with", expressed_Principle, "BUT, if you keep savings, you will have ", expressed_Amount_Of_Money, "in your account after the specified period of time!")		#Final Output