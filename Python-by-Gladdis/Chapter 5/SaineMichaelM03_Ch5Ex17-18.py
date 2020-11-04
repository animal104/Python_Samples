#Mickey "Bad Nerd" Saine
#SDEV 140
# This program is the culmulation of two programs. One to determine if a number is prime and another to list all the primes between 0-100
#06 September 2020



import time
import datetime
import math

def intro():																																	#Create my first function to provide my typical witty introductions
    print(f'''Welcome to the Transformers SEARCH FOR THE PRIME!!!''')																			#Provides user with Title
    print(f'''\t \t Version 1.0''') 
    today =datetime.datetime.today()	
    date_Written = datetime.date (2020, 9, 27)																									#Provides the time because I learned about it in a video today, and REALLY liked it, so I included it in my witty intro
    print (f'''\tPatent Pending,{date_Written: %B %d, %Y}''')																					#Changed the Patent Pending to Reflect this newly learned concept of time
    print (''' ''')
    time.sleep(1)
    print('''For Eons, the Noble Autobots have searched for the one who most resembles THE Primus. A glorious creature of pure perfection...''')
    print (''' ''')	
    print('''Therefore, this program is designed to look at the smallest bit of data and determine it's ability to become a PRIME...''')		#Provides User with Lay-man definition of issue 
    print (''' ''')
    time.sleep(1)
    print(f'''You are accessing this program at {today:%H:%M, on %A, %B %d, %Y}''')																#Really just enjoying the time, and want to capture this for later programs
    print (''' ''')
    print (''' ''')
    time.sleep(1)
    
def nameForCredit ():	
    print ('''So let's get started with this simple question that we will match with the computer\'s answer...''')
    print (''' ''')
    name= input('''State your name, for the scrolls in the halls of Telatran One:''')														#Shows name on screen, as per Instructor's Requirement
    print (''' ''')
    print (f'''Well, {name}. This name has been recorded. So, it shall stand in the scrolls of Teletran One!''', sep="")
    print (''' ''')

def is_prime(num):
   for i in range(2,num):
       if (num % i) == 0:
           break
   else:
       print(num,"is a prime number")      


def primus():																																#Function to process all the information that was derived from the prime function
    print (f'''Now, is when we find a out if a number has the primus (by being prime) or does not. If the number does not, then we won't even speak of it again.''')
    print (''' ''')
    print (f'''If it is unworthy, then I won't even tell you the answer to your question, because it is beneath me!''')
    print (f'''Are you ready?''')
    print (''' ''')
    num = int(input('''Enter your choice for a number to determine it's probability of being a PRIME: '''))									#input for question 17. I know that it said that I could just submit Q18, but somehow it just didn't make sense to me without the line
    is_prime(num)
	
    print (''' ''')
    print (f'''Now that we have determined that number's ability, or inability, to show it's true primus, I am now prepared to show you ALL the numbers that do have the primus.''')
    print (f'''Are you ready?''')
	
    print (''' ''')	
    for num in range(1,101):
        if is_prime(num):
            print(num)
			
def main():
    intro()																																		#intro is called and played out. I'm sure the jokes were waaayyy better the rerun version
    name = nameForCredit()																														#A call to the name function and brining forward the name that was returned
    primus()
	


main()