#Mickey "Code Monkey" Saine
#SDEV 140
# This program is designed to read the content of two files into two separate list and determine whether or not the user name is among the list of most popular names

import time
import datetime

def intro():																																												#Create my first function to provide my typical witty introductions
    print('''Welcome to the Number Popularity Quiz! ''')																																	#Provides user with Title
    print('''\t \t Version 1.0''') 
    today =datetime.datetime.today()	
    date_Written = datetime.date (2020, 10, 8)																																				#Provides the time because I learned about it in a video today, and REALLY liked it, so I included it in my witty intro
    print (f'''\tPatent Pending,{date_Written: %B %d, %Y}''')																																#Changed the Patent Pending to Reflect this newly learned concept of time
    print (''' ''')
    time.sleep(1)
    print('''This program is designed to take a selected name and determine if was a popular boy/girl/both name for the years 2000-2009.''')												#Provides User with Lay-man definition of issue 
    print (''' ''')
    time.sleep(1)
    print(f'''You are accessing this program at {today:%H:%M, on %A, %B %d, %Y}''')																											#Really just enjoying the time, and want to capture this for later programs
    print (''' ''')
    time.sleep(1)
    
def nameForCredit():	
    print (''' ''')
    name= input('''Before we start, can I get YOUR name for the results:''')																												#Shows name on screen, as per Instructor's Requirement
    return name

def list():
    infile = open('BoyNames.txt', 'r')																																						#Open the BoysName's file for processing
    boysNames = infile.readlines()																																							#read the contents of the file and store in a variable for the Boys names
    infile.close()																																											#close the BoysName's file
    for index in range (len(boysNames)):																																					#Strip the individual lines
        boysNames[index] = boysNames[index].rstrip('\n')
	

    infile = open('GirlNames.txt', 'r')																																						#Open the GirlsNames's file for processing
    girlsNames = infile.readlines()																																							#read the contents of the file and store in a variable for the girls names
    infile.close()																																											#close the GirlName's file
    for index in range (len(girlsNames)):																																					#Strip the individual lines
        girlsNames[index] = girlsNames[index].rstrip('\n')

    allNames = []																																											#creation of a new list
    for item in boysNames:																																									#for statement to append the boy's names to the new list
        allNames.append(item)
    for item in girlsNames:																																									#for statement to append the girl's names to the new list
        allNames.append(item)


    search = input ('''Please enter the name that you wish to check:''') 
    print(''' ''')
    print(f'''Well, that is an extremly well thought out name!''')
    print(''' ''')
						
    print(f'''We can check these names via boys names, girl's names, or just both names''')

	
    print(f'''You may select from the following options: Boys <1> , Girls <2>, Both <3>''')
    print (''' ''')
    choice = input(f'''Please select the corresponding list option now: ''')																													#Prompt the user to choose which list to check
    print(''' ''')
	
	
	
    if choice == "1":																																											#if-else statement to check each of the lists depending on their election
        if search in boysNames:
            print(f'''{search} was found to be one of the most popular boy's names within the United States from 2000-2009''')
        else: 
            print(f'''I'm so sorry! {search} was not found to be one of the most popular boy's names within the United States from 2000-2009''')
    elif choice == "2":
        if search in girlsNames:
            print(f'''{search} was found to be one of the most popular girl's names within the United States from 2000-2009''')
        else: 
            print(f'''I'm so sorry! {search} was not found to be one of the most popular girl's names within the United States from 2000-2009''')
    else:
        if search in allNames:
            print(f'''{search} was found to be one of the most popular names within the United States from 2000-2009''')
        else: 
            print(f'''I'm so sorry! {search} was not found to be one of the most popular names within the United States from 2000-2009''')
		
		


def main():
    intro()																																		#Plays out my dorky introductions
    name = nameForCredit()																														#A call to the name function and brining forward the name that was returned
    print (''' ''') 
    print (f'''Well, {name}. What a lovely name. Let's starting looking at the name you want to check tho!''', sep="")							#the return statement to show the name for the credit 
    time.sleep(2)
    print (''' ''')
    list()

main()	


