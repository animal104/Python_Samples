#Mickey "Code Monkey" Saine
#SDEV 140
# This program is designed to determine the total price with a state sales tax of 5% and a county sales tax of 2.5%
#06 September 2020



import time

print('Welcome to the County and State Sales Tax Comprimication Procolmation Caluculator...')		#Provides user with Title
print('version 1.0') 																				#Provides Version Number
print ('')
time.sleep(1)
print('This program is designed to make sure that those prices you saw on the shelf are not the same as your total...')
print ('')
time.sleep(1)
print ('')
print ('Patent pending, 2020')
print ('')
time.sleep(1)
print ('So let\'s get started with this simple question that we will match with the computer\'s answer...')
print ('')
name= input("What is your first and last name to ensure it's on this form for credit:")				#Shows name on screen, as per Instructor's Requirement
print ('')
print ('Well, ', name, '. That first answer checks out!', sep='')


price=float(input('What is the total for your purchase today?:'))									#get the purchase amount

print ('')
print ('')
time.sleep(1)
print ('Wow, Really? That\'s not bad. No wait, there\'s something missing, let\'s look into that')

print ('')
print ('')
time.sleep(1)
print ('Oh wait, I forgot your total!!')

print ('')
print ('')
time.sleep(1)
print ('Just a moment, gotta look up that tax rate')

print ('')
print ('')
time.sleep(1)


print ('C\'mon, I went to public school after all!')

print ('')
print ('')
time.sleep(2)

print ('Ah! Got it!')

print ('')
print ('')
time.sleep(2)

state_Sales_Tax = price * 0.025																#Establish the State Sales Tax
county_Sales_Tax = price * 0.05																#Establish the County Sales Tax
total_Sales_Tax = state_Sales_Tax + county_Sales_Tax										#determine how much the customer actually pays in taxes

expressed_Total_Sales_Tax = "{:,.0%}".format(total_Sales_Tax)								#format variable to money for readability


total_purchase = float(price + total_Sales_Tax)												#Define the Total Purchase Price

expressed_Price= "${:,.2f}".format(price)													#express the purchase price of the item into a readable format
expressed_Purchase= "${:,.2f}".format(total_purchase)										#express that entire purchase price into a readable format
expressed_State_Sales_Tax= "${:,.2f}".format(state_Sales_Tax)													#express the purchase price of the item into a readable format
expressed_County_Sales_Tax= "${:,.2f}".format(county_Sales_Tax)										#express that entire purchase price into a readable format


print ('It\'s my apologies, but I must inform you that there is a 5 percent state sales tax!')
print ('')
print ('')
time.sleep(2)

print ('There\'s actually more bad news. I have to let you know that there is also a 2.5 percent county sales tax.')
print ('')
print ('')
time.sleep(1)

print ('Therefore I must let you know that your total purchase today was ', price, '.', sep = '')
print ('')
print ('Your State Sales tax equaled ', expressed_State_Sales_Tax, ".", sep = '')								#supporting state tax amount so the customer has an idea where the amount came from
print ('')
print ('Your County Sales tax equaled ', expressed_County_Sales_Tax, ".", sep = '')							#supporting county tax amount so the customer has an idea where the amount came from
print ('')
print ('Therefore, your total purchase price is ', expressed_Purchase, '.', sep = '')			#Final Output answering the question
time.sleep(2)
print ('')
print ('')
print ('Is this acceptable?')
print ('')
print ('')
time.sleep(1)
print ('Thank you! Come Again!')