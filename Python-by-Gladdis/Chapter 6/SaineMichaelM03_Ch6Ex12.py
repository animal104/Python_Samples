#Mickey "gets his steps from Pokemon Go!" Saine
#SDEV 140
# This program is designed to reads the steps from a file and calculate the average of steps for that year in a monthly range
#04 October 2020

import time
import datetime

def intro():																																	#Create my first function to provide my typical witty introductions
    print('''Welcome to the Step Fitter Getter Averager Thing-a-mom-bob...''')																	#Provides user with Title
    print('''\t \t \t Version 1.0''') 
    today =datetime.datetime.today()	
    date_Written = datetime.date (2020, 9, 27)																									#Provides the time because I learned about it in a video today, and REALLY liked it, so I included it in my witty intro
    print (f'''\t\tPatent Pending,{date_Written: %B %d, %Y}''')																					#Changed the Patent Pending to Reflect this newly learned concept of time
    print (''' ''')
    time.sleep(1)
    print('''This program is designed to read your steps and average them on a per moth basis to understand when you steps the best...''')		#Provides User with Lay-man definition of issue 
    print (''' ''')
    time.sleep(1)
    print(f'''You are accessing this program at {today:%H:%M, on %A, %B %d, %Y}''')																#Really just enjoying the time, and want to capture this for later programs
    print (''' ''')
    print (''' ''')
    time.sleep(1)
    
def nameForCredit():	
    print ('''Please give the Stepper's Name: (First and Last):''')																				#Get input for name to show on screen
    print (''' ''')
    name= input('''What is your first and last name to ensure it's on this form for credit:''')													#Shows name on screen, as per Instructor's Requirement
    return name

def steps():

    month = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December')
		 
    days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
	
    stepCounter = open('steps.txt', 'r')																										#Opens the text document to get the steps
    monthCount = 0																																#Zeros out the month count for initialization

    for num in range(1, 13):																													#Creates Each month with a total of 9 steps, 0 count, and zero average
        totalSteps = 0
        count = 0
        average = 0

        for count in range(1, days[monthCount] + 1):																							#Reads the month and days in the month
            steps = int(stepCounter.readline())																									#Assigns an integar number as read from each line
            totalSteps = totalSteps + steps																										#Creates the total steps
            average = totalSteps / days[monthCount]
        print ('The average steps taken for the month of ' + month[monthCount] +
               ' is: ' + format(average, ',.1f') + ' steps.\n')																					#Prints the requested information for the month to start again

        monthCount = monthCount + 1																												#Increments the month count
		
def main():																																		#Defines the main class
    intro()																																		#Plays out my dorky introductions
    name = nameForCredit()																														#A call to the name function and brining forward the name that was returned
    print (''' ''')
    print (f'''Well, {name}. That first answer checks out! Let's hope this bodes well for the rest of your fitness goals''', sep="")			#the return statement to show the name for the credit 
    print (''' ''')
    print ('\t\tAVERAGE STEPS TAKEN PER MONTH')
    print ('__________________________________________________________________')
    print ('')
    steps()

main()																																			#execution of main class