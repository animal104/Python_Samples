#Mickey "and tab and mountain dew" Saine
#SDEV 220
# This program is designed to create an Account object with an account id of 3345, a balance of $35,000, and an annual interest rate of 4.5%. Use the withdraw method to withdraw $2,500, use the deposit method to deposit $3,000, and print the id, balance, monthly interest rate, and monthly interest.
#20 September 2020



import time
from account import Account

#print("Welcome to the Dunder Mifflin's Software Division Discount shopping shoporama...")																#Provides user with Title
#print("version 1.0") 																																	#Provides Version Number
#print ("")
#time.sleep(1)
#print("This program is designed to test an Account Object with a series of Random and exciting variables...")											#Provides User with Lay-man definition of issue 
#print ("")
#time.sleep(1)
#print ("")
#print ("Patent pending, 2020")
#print ("")
#time.sleep(1)
#print ("Well, Good morning!. Welcome to Dunder Mifflin Software Sales. My name is Dwight, and I'd be happy to help you!", sep="")
#print ("")
#print ("Well, I'll assume that you are calling about one of our fine software packages at retail for $99.00, but I might be able to do a little better depending on how much you order.")

def main():																																				#Defines main Function
    acc = Account(3345, 35000, 4.5)																														#Reaches back and inputs information from the functions defined in account.py
    acc.withdraw(2500)
    getAccountInfo(acc)
    acc.deposit(3000)
    getAccountInfo(acc)


def getAccountInfo(acc):																																#defines the account info function
    id = acc.getId()
    bal = acc.getBalance()
    mir = acc.getMonthlyInterestRate()
    mi = acc.getMonthlyInterest()
    print("Account ID:", id, "\nBalance:", bal,
          "\nMonthly IR:", mir, "\nMonthly interest:", mi)																								#prints the statement of requested items


main()																																					#calls the previous function and executes it 