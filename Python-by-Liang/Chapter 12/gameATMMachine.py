#Mickey "STILL likes fritos" Saine
#SDEV 220
# This program is designed to create a game using the Account class to stimulate an ATM Machine
#18 October 2020

import time																												#import time for my witty intro
import datetime																											#import date-time because that whole Linux mathematical stuff was silly and I like this one better

def intro():																											#Create my first function to provide my typical witty introductions. 
    print (f'''\t \t \t Welcome to Ivy Tech Credit Union ATM''')
    print (f''' \t \t ---------------------------------------------------''')			
    print('''\t \t\t\t Version 1.0''') 
    today =datetime.datetime.today()	
    date_Written = datetime.date (2020, 10, 18)																			#Provides the time because I learned about it in a video today, and REALLY liked it, so I included it in my witty intro
    print (f'''\t\t\tPatent Pending,{date_Written: %B %d, %Y}''')														#Changed the Patent Pending to Reflect this newly learned concept of time
    time.sleep(1)
    print (f''' \t \t ---------------------------------------------------''')	  
    print(f'''You are accessing this program at {today:%H:%M, on %A, %B %d, %Y}''')										#Really just enjoying the time, and want to capture this for later programs
    time.sleep(1)
    print (''' ''')
    print(f'''Be aware that tampering with ATM systems could end with being forced to watch 5-50 hours of JoJo Siwa''')
    print (''' ''')
    time.sleep(1)

class Account:																											#Defines the class created for the program testing
    def __init__(self,id=0,balance=500,annualIntersetRate=0):															#Defines the variables necessary to execute
        self.__id = id
        self.__balance = balance
        self.__annualIntersetRate = annualIntersetRate

    def getId(self):																									#Defines the attributes that that command can do such as get id 
        return self.__id																								#defines the action taken with the attribute given

    def getBalance(self):
        return self.__balance																							#defines the action taken with the attribute given. 

    def getAnnualIntersetRate(self):
        return self.__annualIntersetRate																				#defines the action taken with the attribute given. 

    def setId(self,id):
        self.__id = id

    def setBalance(self,balance):
        self.__balance = balance

    def setAnnualIntersetRate(self,annualIntersetRate):
        self.__annualIntersetRate = annualIntersetRate																	#defines the action taken with the attribute given.  

    def getMonthlyInterestRate(self):
        return (self.__annualIntersetRate/ 12) /100																		#defines the action taken with the attribute given.  

    def getMonthlyInterest(self):
        return self.__balance *self.getMonthlyInterestRate()															#defines the action taken with the attribute given.  

    def deposit(self,balance):
        self.__balance += balance																						#defines the action taken with the attribute given.  

    def withdraw(self,amount):
        self.__balance -= amount																						#defines the action taken with the attribute given.  



def main():																												#Defines the main function to get the program to work	
    intro()
    accounts = []																										#creates my account empty list for fulfillment
    for i in range(10):																									#Allows me to put the account information into the list with 9 items
        ac = Account(i)
        accounts.append(ac)																								#appends the information

    count = 0

    while count < 100:																									#Yeah, there are other ways I could have done this, but It was funny to use the infinite loop from Chapt 5 word for work. 
        id = int(input('''Please enter your account number now: '''))													#input for account number

        while (True):																									#while statement to decide which of the items that I'm actually doing depending on the account number being right AND the right choices is made
            if 0 <= id <= 9:																							#nested if statement that does the heavy lifting
                print(f'''\n \t MAIN MENU''')																			#Main menu with the requested options
                print(f'''-------------------------''')
                print(f'''1: Check Your Balance''')
                print(f'''2: Withdraw Funds from your account''')
                print(f'''3: Deposit additional funds''')
                print(f'''4: Exit''')

                choice = int(input(""))
                if choice == 1:																							#If statement based on the number choose by the person working with it, decides which line that the program will interpret
                    print(''' ''')
                    print(f'''The listed balance for this account is ${accounts[id].getBalance()}.''')
                elif choice == 2:
                    amount = float(input(f'''Enter an amount that you wish to withdraw: '''))
                    accounts[id].withdraw(amount)
                elif choice == 3:
                    amount = float(input(f'''Enter an amount to deposit: '''))
                    accounts[id].deposit(amount)
                elif choice == 4:
                    print(''' ''')
                    print (f'''Thank you! Come Again!''')
                    print (''' ''')
                    intro()
                    break																								#Break Statement to exit
            else:
                print('''I'm sorry, that number is not recognized by the system''')										#Final else to validate the input
                break

main()																													#executes the main function