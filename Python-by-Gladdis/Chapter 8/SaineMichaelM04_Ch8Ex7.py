#Mickey "Code Monkey" Saine
#SDEV 140
# This program is designed to read the content of a files and return information such as number of uppercase, lowercase, digits and white spaces found
#18Oct2020

import time
import datetime

def intro():																																												#Create my first function to provide my typical witty introductions
    print('''Welcome to the Sentence reading whitespaces tabulating, uppercase counting, lowercase evaluating app! ''')																		#Provides user with Title
    print('''\t \t\t\t Version 1.0''') 
    today =datetime.datetime.today()	
    date_Written = datetime.date (2020, 10, 8)																																				#Provides the time because I learned about it in a video today, and REALLY liked it, so I included it in my witty intro
    print (f'''\t\t\tPatent Pending,{date_Written: %B %d, %Y}''')																															#Changed the Patent Pending to Reflect this newly learned concept of time
    print (''' ''')
    time.sleep(1)
    print('''This program is designed to read a paragraph in a text file and return formal elements about said paragraph.''')																#Provides User with Lay-man definition of issue 
    print (''' ''')
    time.sleep(1)
    print(f'''You are accessing this program at {today:%H:%M, on %A, %B %d, %Y}''')																											#Really just enjoying the time, and want to capture this for later programs
    print (''' ''')
    time.sleep(1)
    
def nameForCredit():	
    print (''' ''')
    name= input('''Before we start, can I get a name for the person requesting this information:''')																						#Shows name on screen, as per Instructor's Requirement
    return name

def list():
    infile=open("text.txt", "r")																																							#Open the file for processing
    
    lines=infile.read().splitlines()																																						#read the contents of the file and store in a variable 
    

    uppercaseNumber=0																																										#Establish variables to count into
    lowercaseNumber=0
    digitsNumber=0
    whiteSpaceNumber=0
    

    for line in lines:																																										#loop statement to calculate the requested Variables
        for ch in line:																																										#Nested Loop Statement to answer the different choices
            if ch.isupper():
                uppercaseNumber+=1
            elif ch.islower():
                lowercaseNumber+=1
            elif ch.isdigit():
                digitsNumber+=1
            elif ch.isspace():
                whiteSpaceNumber+=1
                
    print( ''' \tThe results are tabulated as follows:''')
    print ('''----------------------------------------------------------------- ''')
    print(f'''The number of uppercase letters contained in the file is {uppercaseNumber}.''')																								#Final Answers
    print(f'''The number of lowercase letters contained in the file is {lowercaseNumber}.''')
    print(f'''The number of digits contained in the file is {digitsNumber}.''')
    print(f'''The number of whitespace characters contained in the file is {whiteSpaceNumber}.''')
                


def main():
    intro()																																													#Plays out my dorky introductions
    name = nameForCredit()																																									#A call to the name function and brining forward the name that was returned
    print (''' ''') 
    print (f'''Well, {name}. That checks out. Let's starting looking at this paragraph!''', sep="")																							#the return statement to show the name for the credit 
    time.sleep(2)
    print (''' ''')
    list()

main()	


