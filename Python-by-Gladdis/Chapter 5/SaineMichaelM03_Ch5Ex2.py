#Mickey "Nerdcore for life!" Saine
#SDEV 140
# This program is designed to determine the total price with a state sales tax of 5% and a county sales tax of 2.5%
#27 September 2020

import time
import datetime
import math


def intro():																																	#Create my first function to provide my typical witty introductions
    print('''Welcome to the REVISED County and State Sales Tax Comprimication Procolmation Caluculator...''')									#Provides user with Title
    print('''\t \t \t Version 2.0''') 
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
    print ('''So let's get started with this simple question that we will match with the computer\'s answer...''')								#Get input for name to show on screen
    print (''' ''')
    name= input('''What is your first and last name to ensure it's on this form for credit:''')													#Shows name on screen, as per Instructor's Requirement
    return name
 
def priceInput():																																#First Function designed to get the purchase prices. Was enterily aggrivated that I couldn't put it all on one function, but tried for hours anyway!
    price = float(input(f"What is the total for your purchase today?:"))																		#User input		
    return price																																#newly created variable
 
def calStateSalesTax(price):																													#I could only get one variable to return from a function so I cared another for the State Sales Tax
    state_Sales_Tax = price * 0.05																												#calculation to get sales tax information
    return state_Sales_Tax																														#the returned variable to get sales tax
	
def calCountySalesTax(price):																													#function to compute and return the county sales tax
    county_Sales_Tax = price * 0.025
    return county_Sales_Tax
	
def calTotalSalesTax(state_Sales_Tax, county_Sales_Tax):																						#next function that calculates and returns the total sales tax
    total_Sales_Tax = state_Sales_Tax + county_Sales_Tax
    return total_Sales_Tax

def calTotalSales(price, state_Sales_Tax, county_Sales_Tax):																					#Final "variable" function to determine the Total Sales
    total_Sales = price + state_Sales_Tax + county_Sales_Tax
    return total_Sales

def answer(reply):	
    if reply == 'y':																															#Defines a new form of question that came with the end of my last program
        print (f'''Thank you! Come Again!''')
    else:
        print (f'''Oh, I am so sorry sir! That is the best we can offer!''')
		
def main():																																		#Function to wrap everything together
    intro()																																		#intro is called and played out. I'm sure the jokes were waaayyy better the rerun version
    name = nameForCredit()																														#A call to the name function and brining forward the name that was returned
    print (''' ''')
    print (f'''Well, {name}. That first answer checks out!''', sep="")																			#the return statement to show the name for the credit 
    print (''' ''')
	
    price=priceInput()																															#Next function that starts off the set of functions to determine prices, taxes and totals. Can I call a function to make my comments too?
    expressed_Price= "${:,.2f}".format(price)																									#The number called is formatted here becasue it got really grumpy everytime I tried to return two variables 
    print(f'''Ahhh, The amount of the purchase was {expressed_Price}''')																		#The expressed response from the input
    print ('')
    print ('')
    time.sleep(2)
	
    print (f'''It's my apologies, but I must inform you that there is a 5% State sales tax!''')													#function for sales tax that works the same as the price function
    state_Sales_Tax=calStateSalesTax(price)
    expressed_State_Sales_Tax= "${:,.2f}".format(state_Sales_Tax)	
    print(f"The state sales tax:",expressed_State_Sales_Tax)
    print ('')
    print ('')
    time.sleep(1)

    print (f'''There\'s actually more bad news. I have to let you know that there is also a 2.5% County sales tax.''')							#function for county tax that works the same as the last two
    county_Sales_Tax=calCountySalesTax(price)
    expressed_County_Sales_Tax= "${:,.2f}".format(county_Sales_Tax)	
    print(f"The state sales tax:",expressed_County_Sales_Tax)
    print ('')
    print ('')
    time.sleep(1)
	
    total_Sales_Tax = calTotalSalesTax(state_Sales_Tax, county_Sales_Tax)																		#function to call the totals. These were put together, since I wanted the return statement to reflect both variables returned
    expressed_Total_Sales_Tax= "${:,.2f}".format(total_Sales_Tax)
    total_Sales=calTotalSales(price, state_Sales_Tax, county_Sales_Tax)
    expressed_Total_Sales= "${:,.2f}".format(total_Sales)	
    print (f'''Therefore, the total Sales tax involved will be {expressed_Total_Sales_Tax}, which makes your total purchase price is {expressed_Total_Sales}.''')

    print(''' ''')
    reply = str(input(f'''Is that price acceptable?(y/n): ''')).lower().strip()																	#Answers that fine question with a different little slice!
    answer(reply)
	
	
main()																																			#The moment of joy in my life, as all these modules execute!

