#Mickey "Pushed More Boots than Green Lantern Killowog!" Saine
#SDEV 140
# This program is designed to calculate the average of the numbers stored in a file and raise exceptions as needed
#04 October 2020

import time
import datetime

def intro():																																	#Create my first function to provide my typical witty introductions
    print('''Welcome to the Number Unpakcer restorer and Averager...''')																		#Provides user with Title
    print('''\t \t \t Version 1.0''') 
    today =datetime.datetime.today()	
    date_Written = datetime.date (2020, 9, 27)																									#Provides the time because I learned about it in a video today, and REALLY liked it, so I included it in my witty intro
    print (f'''\t\tPatent Pending,{date_Written: %B %d, %Y}''')																					#Changed the Patent Pending to Reflect this newly learned concept of time
    print (''' ''')
    time.sleep(1)
    print('''This program is designed to make sure that those prices you saw on the shelf are not the same as your total...''')					#Provides User with Lay-man definition of issue 
    print (''' ''')
    time.sleep(1)
    print(f'''You are accessing this program at {today:%H:%M, on %A, %B %d, %Y}''')																#Really just enjoying the time, and want to capture this for later programs
    print (''' ''')
    print (''' ''')
    time.sleep(1)
    
def nameForCredit():	
    print ('''So let's get started with the wonderful task of getting a name...''')																#Get input for name to show on screen
    print (''' ''')
    name= input('''What is your first and last name to ensure it's on this form for credit:''')													#Shows name on screen, as per Instructor's Requirement
    return name
	
def numbers():

    try:																																		#calls the try method in case the file is missing
        infile = open('numbers.txt', 'r')																										#opens and reads the number text file
        
        num1 = int(infile.readline())																											#Assigns the Number to the first variable
        
        num2 = int(infile.readline())																											#Assigns the Number to the second variable

        num3 = int(infile.readline()) 																											#Assigns the Number to the third variable   

        infile.close()																															#closes the files
		
        total = num1 + num2 + num3																												#Totals the three numbers

        average = total/3																														#averages the three numbers

        
    except IOError:																																#Provides exception error if the files isn't there
        print("An error occurred trying to read " + \
              "the file", filename)

    try:																																		#calls the try method in case the Values were not found in the file
        print('The numbers published to the files were ', num1, ', ', num2, ', ', num3, '.', sep ='')
        print (''' ''')
        print('The total derived from these numbers were ', total, '.', sep ='')
        print (''' ''')
        print('This averaged out to an average of ', average, '.', sep ='')
        print (''' ''')		
		
    except ValueError:
	
        print('ERROR: The numbers were found to be not valid within the file.')


def main():																																		#Definition of main class
    intro()																																		#intro is called and played out. I'm sure the jokes were waaayyy better the rerun version
    name = nameForCredit()																														#A call to the name function and brining forward the name that was returned
    print (''' ''')
    print (f'''Well, {name}, it's wonderful to meet you. Noted!''', sep="")																		#the return statement to show the name for the credit 
    print (''' ''')	
    numbers()																																	#invoke the number class
	
main()																																			#Execution of main class

