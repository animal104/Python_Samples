#Mickey "Code Monkey" Saine
#SDEV 140
# This program is designed to Ask a user to enter the stores sales and then use a loop to calculate the total sales for the week and display the result
#11 October 2020

import time
import datetime

def intro():																																	#Create my first function to provide my typical witty introductions
    print('''Welcome to the Legion of Doom Mass Weapons Employee Portal ''')																	#Provides user with Title
    print('''\t \t Version 1.0''') 
    today =datetime.datetime.today()	
    date_Written = datetime.date (2020, 10, 8)																										#Provides the time because I learned about it in a video today, and REALLY liked it, so I included it in my witty intro
    print (f'''\tPatent Pending,{date_Written: %B %d, %Y}''')																					#Changed the Patent Pending to Reflect this newly learned concept of time
    print (''' ''')
    time.sleep(1)
    print('''This program is designed to get the store sales and calculate the total PROFITS OF EVILLLLLLL...''')								#Provides User with Lay-man definition of issue 
    print (''' ''')
    time.sleep(1)
    print(f'''You are accessing this program at {today:%H:%M, on %A, %B %d, %Y}''')																#Really just enjoying the time, and want to capture this for later programs
    print (''' ''')
    time.sleep(1)
    
def nameForCredit():	
    print (''' ''')
    name= input('''Before recording sales, please enter the recording Henchmen's first and last name:''')										#Shows name on screen, as per Instructor's Requirement
    return name

def sales():
    NUM_DAYS = 7																																#Variable to establish number of items in the list
    sales = [0] * NUM_DAYS																														#Creation of a blank list for the purpose of getting inputs
	  
    print (f'''Now, you are ORDERED to enter the number of sales for this week:''')																#Gets the sales for the day
    print ('''__________________________________________________________________ ''')
	
	
    for index in range (len(sales)): 																											#loop for inputing the data
        sales[index] = float(input(f'''Day {index+1} Sales:  '''))
	
    total = 0																																	#initiation of total variable
	
    for value in sales:																															#loop for retrieving the items in the loop and calculating them
        total += value

    expressed_Total= "${:,.2f}".format(total)																									#Appropriately format the total for readability
	
    print (''' ''')
    
    time.sleep(1)
    print(f'''Our records now show that {expressed_Total} in profits were submitted.''')														#Final Answer
    print (''' ''')

    print ('''__________________________________________________________________ ''')		
    print (f'''Excellent Work! That was a great amount of money for the purpose of gathering EVIL! Darksied is proud!''')						
    print (''' ''')
	
    print(f'''All profits will go towards finding the final truth of the Anti-life Equation.''')												
    time.sleep(2)
	
    print (''' ''')	
    print (''' ''')
    print(f'''All hail Darkseid!''')														
	
def main():
    intro()																																		#Plays out my dorky introductions
    name = nameForCredit()																														#A call to the name function and brining forward the name that was returned
    print (''' ''')
    print (f'''........authenticating''')
    time.sleep(1)
    print (f'''process user name....''')
    time.sleep(1)
    print (f'''Well, Henchmen {name}. The user is authenticated. Stand by for the implementation of further instruction''', sep="")				#the return statement to show the name for the credit 
    time.sleep(2)
    print (''' ''')
    sales()
	
main()