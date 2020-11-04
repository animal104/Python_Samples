#Mickey "and tab and mountain dew" Saine
#SDEV 140
# Write a program that uses nested Loops to draw a specified pattern 
#20 September 2020



import time

print("Welcome to the graphical Interfacing Star Wars factorial Field....")													#Provides user with Title
print("version 1.0") 																										#Provides Version Number
print ("")
time.sleep(1)
print("This program is designed to create an asteroid field to hide from the evil empire...")								#Provides User with Lay-man definition of issue 
print ("")
time.sleep(1)
print ("Patent pending, 2020")
print ("")
time.sleep(1)
print ("So let\'s get started with this simple question that we will match with the computer\'s answer...")
print ("")
name= input("What is your first and last name, kid? My Wookie wants to know:")												#Shows name on screen, as per Instructor's Requirement
print ("")
print ("Well, ", name, ". You got the part! I like you kid! The Hyperspace drive isn't working, so we need to find somewhere else to hide!", sep="")
print ("")
print ("So, ", name, ". Since you got that right, can I draw a triangle patterns Star field for you?")
print ("")
print ("I bet you I can get it done in under a parsec")
print ("")
print ("")
time.sleep(1)
print ("Great! Let's get this done!")
print ("")
time.sleep(2)


base_Row = 7

for rows in range(base_Row, 0, -1):																							#First Loop to create my rows
    for col in range(1, rows + 1):																							#nest loop to create the columns
        print("*", end=" ")																									#print the individual lines of the pyramid
    print('\r')																						

print ("")
time.sleep(1)	
print ("See, that wasn't so bad kid!. Go back with Chewy and help him get that hyper...")
print ("")
print("... Waiiittt, What is the there!")