#Mickey "Plegius the Wise" Saine
#SDEV 140
# This program is designed implement a function named max that accepts two integer values as arguments and returns the value that is greater of the two
#27 September 2020

import time
import datetime
import math

def intro():																																	#Create my first function to provide my typical witty introductions
    print('''Welcome to the Integarial Battle Royale of the Pythonic Ages of Arguing...''')														#Provides user with Title
    print('''\t \t \t Version 2.0''') 
    today =datetime.datetime.today()	
    date_Written = datetime.date (2020, 9, 27)																									#Provides the time because I learned about it in a video today, and REALLY liked it, so I included it in my witty intro
    print (f'''\t\tPatent Pending,{date_Written: %B %d, %Y}''')																					#Changed the Patent Pending to Reflect this newly learned concept of time
    print (''' ''')
    time.sleep(1)
    print('''The program is designed to choose two Integars and allow them to step into the field of battle to determine the greaters of the two...''')	#Provides User with Lay-man definition of issue 
    print (''' ''')
    time.sleep(1)
    print(f'''You are accessing this program at {today:%H:%M, on %A, %B %d, %Y}''')																#Really just enjoying the time, and want to capture this for later programs
    print (''' ''')
    print (''' ''')
    time.sleep(1)
    
def nameForCredit ():	
    print ('''So let's get started with this simple question that we can take your bet...''')
    print (''' ''')
    name= input('''What is your first and last name to ensure it's on this form for credit:''')													#Shows name on screen, as per Instructor's Requirement
    print (''' ''')
    print (f'''Well, mighty {name}. That first answer checks out!''', sep="")
    print (''' ''')
	
def max(num1, num2):																															#creates function to compare the two numbers
    if num1 > num2:																																#if else statment to compare the two numbers
        return num1
    else:
        return num2


def main():																																		#Function to wrap everything together
    intro()																																		#intro is called and played out. I'm sure the jokes were waaayyy better the rerun version
    name = nameForCredit()																														#A call to the name function and brining forward the name that was returned
    num1 = input("Please enter first integer to compete in this mighty tournament: ")															#Get Answer for first argument for the function
    print (f'''So you are choosing the might {num1}. Excellent Choice!''')
    num2 = input("Please enter second integer to compete in this mighty tournament: ")
    print (f'''Ohhh, I had not considered {num2}. This will be a bout for the ages!''')															#get answer for the second argument for the function
    max_value = max(num1, num2)																													#Call the function and place the two "answers" into it 
    print (''' ''')
    print (''' ''')
    time.sleep(1)
    print (f'''Look at those numbers go!''')
    print (''' ''')
    print (''' ''')
    time.sleep(1)
    print (f'''Hereye! Hereya! The battle had been fought. The assessment has been measured! {max_value} is clearly the winner of this battle!''')#Print the results of the function
	
main()
