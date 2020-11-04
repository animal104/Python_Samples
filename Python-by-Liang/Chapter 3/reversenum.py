#Mickey "sometimes the output stinks" Saine
#SDEV 220
#Write a program that prompts the user to enter a four-digit integer and displays the number in reverse order.  
#06 September 2020

import math
import time

print("Welcome to Atomic Re-scrambling of a Transported Integer.")																											#Defining the project for the user
print("version 1.0") 																																						#Provides Version Number
print ("")
time.sleep(1)
print("This program re=orders the re-ordering of a four digit number into a five digit number in the order 3,2,4,1,5!")														#Define the purpose to the User
print ("")
print("Because Dr. McCoy was right. Sometimes things get scrambling in a transporter")
print ("")
print ("Patent pending, 2020")
print ("")
time.sleep(1)

number=int(input("Please enter a five digit integer:"))																														#get the number to reorder

number5 = int(number/1 %10)																																					#break the number into multiple integars so they can be reordered
number4 = int(number/10 %10)
number3 =  int(number/100 %10)
number2 = int(number/1000 %10)
number1 = int(number/10000 %10)

print("")
print("Well, that was an interesting transformation.")
print ("")
time.sleep(1)


print("According to my calculations, the number went from ", number, " all the way to scrambled value of ", number3, number2, number4, number1, number5, ".", sep="")		#Final output with number order changed