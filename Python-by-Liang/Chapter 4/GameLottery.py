#Mickey "Wondering if the manager wants to write it" Saine
#SDEV 220
#Starting with Lottery.py, generate a three-digit lottery number for users to guess and attempt to win money with.   
#06 September 2020



import random
import math
import time

print("Welcome to the Howell St Lotto Generator...")																	#Defining the project for the user
print("version 1.0") 																									#Provides Version Number
print ("")
time.sleep(1)
print("This is the Final effort of this week (For this class)...")
print ("")
time.sleep(1)
print ("")
print ("Patent pending, 2020")
print ("")
time.sleep(1)
print ("So let\'s get started with this simple question that we will match with the computer's answer...")
print("If you win, you get:")																							#Define the purpose to the User
print("Exact match: you win $15,000")
print("Match all digits, but not in the right order: you win $7,500")
print("Two of the Digits were matched: you win $2,000")
print("Match one digit or none: You didn't win this time! Please try again!")
time.sleep(1)
print ("")
print ("Ready to get this started?")

# Generate a lottery number

lottery = random.randint(0, 999) 																						#creates the random number to judge as a Lottery


 
# Prompt the user to enter a guess																						#receives the user guess
guess = eval(input("Enter your lottery pick (Three digits): ")) 

 
# Get digits from lottery
lotteryDigit1 = int(lottery/100 %10)																					#converts the lottery number into three integers
lotteryDigit2 = int(lottery/10 %10)
lotteryDigit3 = int(lottery/1 %10)
 
# Get digits from guess
guessDigit1 = int(guess/100 %10)																						#converts the user guess into three integers for comparison
guessDigit2 = int(guess/10 %10)
guessDigit3 = int(guess/1 %10)

guess1 = bool((lotteryDigit1 == guessDigit1) or (lotteryDigit1 == guessDigit2) or (lotteryDigit1 == guessDigit3))		#uses booleans to compare the broken up integars
guess2 = bool((lotteryDigit2 == guessDigit1) or (lotteryDigit2 == guessDigit2) or (lotteryDigit2 == guessDigit3))
guess3 = bool((lotteryDigit3 == guessDigit1) or(lotteryDigit3 == guessDigit2) or (lotteryDigit3 == guessDigit3))

print ("The Lottery Numbers were ", lottery, ".", sep="")
 

if guess == lottery: 																									#evaluates the different numbers and gives a final scoring or prize winning
	print("Exact match: you win $15,000")
	
elif (guess1 and guess2 and guess3): 
	print("Match all digits, but not in the right order: you win $7,500")	

	 		

elif (guess1 and guess2)\
	or (guess1 and guess3)\
	or (guess2 and guess3):
	print("Two of the Digits were matched: you win $2,000")
	
elif (guess1)\
	or (guess2)\
	or (guess3):
	print("Match one digit: You didn't win this time! Please try again!")
	
else:
	print("Sorry, no match: You didn't win this time! Please try again!")