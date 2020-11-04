#Mickey "Wonders why he didn't start in this field instead of Carpenter" Saine
#SDEV 140
# This program is designed to generate a series of numbers, store those numbers in a file and read those numbers back
#04 October 2020

import time
import datetime
import random

def intro():																																	#Create my first function to provide my typical witty introductions
    print('''Welcome to the Number Generation and Regenerations Calcumnatice Calculator...''')													#Provides user with Title
    print('''\t \t \t Version 1.0''') 
    today =datetime.datetime.today()	
    date_Written = datetime.date (2020, 9, 27)																									#Provides the time because I learned about it in a video today, and REALLY liked it, so I included it in my witty intro
    print (f'''\t\tPatent Pending,{date_Written: %B %d, %Y}''')																					#Changed the Patent Pending to Reflect this newly learned concept of time
    print (''' ''')
    time.sleep(1)
    print('''This program is designed to generate a series of number, store those numbers and read them back, in case you forgot...''')			#Provides User with Lay-man definition of issue 
    print (''' ''')
    time.sleep(1)
    print(f'''You are accessing this program at {today:%H:%M, on %A, %B %d, %Y}''')																#Really just enjoying the time, and want to capture this for later programs
    print (''' ''')
    print (''' ''')
    time.sleep(1)
    
def nameForCredit():	
    print ('''So let's get started with this simple question that we will match with the computer\'s answer...''')								#Get input for name to show on screen
    print (''' ''')
    name= input('''What is your first and last name to ensure it's on this form in order to ensure I GET CREDIT:''')							#Shows name on screen, as per Instructor's Requirement
    return name
	
def write():																																	#Object class to write the numbers to the file
    object_file = open('random_numbers.txt', 'w')																								#opens a file to write to
	
    how_many = int(input('How many different numbers should we generate today?'))																#gets the input from the user of numbers to make
	
    for i in range(how_many):																													#randomized number generator that creates numbers n the range of 1-500
        number = random.randrange(1, 501)
        number = str(number)																													#turns the objects into streens
        object_file.write(number)																												#Writes the numbers to the files
        object_file.write('\n')																													#Prints a new line between numbers
		
    object_file.close()																															#Closes the files for the next step
	
	
def read():																																		#Object Class to read the files
    object_file = open('random_numbers.txt', 'r')																								#Opens the file to read
    total = 0																																	#Sets total count to normal
    count = 0																																	#Sets count to normal
    for i in object_file: 																														#for statement to account for all the numbers
        i = i.rstrip('\n')																														#Strips the statements of the new line
        i = int(i)																																#makes the statments integars again
        print(i)																																#Prints the number
        total += i																																#Total is incremented by one
        count += 1																																#Count is incremented by one

    print ('__________________________________________________________________')
    print ('''''')		
    print('Your choices led to the generation of ', count, ' numbers.', sep='')
    print ('''''')	
    print('Those numbers generated equaled a full sum of ', total, '.', sep='')
    print ('''''')	
    print('HOWEVER COMMA...Next time, can we generate a REAL number for some more difficulty?')
	
    object_file.close()
	
	
def main():																																		#Definition of main class
    intro()																																		#Plays out my dorky introductions
    name = nameForCredit()																														#A call to the name function and brining forward the name that was returned
    print (''' ''')
    print (f'''Well, {name}. Let's start a Generating some numbers now''', sep="")																#the return statement to show the name for the credit 
    print (''' ''')		
    write()
    print('THE NUMBERS GENERATED FROM YOUR CHOICES WERE')
    print ('__________________________________________________________________')
    print ('''''')	
    read()
	
main()																																			#execution of main class																															#execution of main class