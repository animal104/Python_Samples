#Mickey "very simple man" Saine
#SDEV 140
# A program that calculates the amount of money a person would earn over a period of time if him/her salary is one penny and doubles from there
#20 September 2020



import time

print("Welcome to the Pennie multiplication re-factoring Income Calculator...")													#Provides user with Title
print("version 1.0") 																											#Provides Version Number
print ("")
time.sleep(1)
print("This program is designed to calculate how much money you could make\
if you doubled your salary from a penny each day...")																			#Provides User with Lay-man definition of issue 
print ("")
time.sleep(1)
print ("")
print ("Patent pending, 2020")
print ("")
time.sleep(1)
print ("So let\'s get started with this simple question that we will match with the computer\'s answer...")
print ('')
name= input("What is your first and last name to ensure it's on this form for credit:")											#Shows name on screen, as per Instructor's Requirement
print ("")
print ("Well, ", name, ". That first answer checks out!", sep="")

day = int (input("So, how many days do you wish to double your pennies while working here?:"))									#take input here. Sets day variable

total = 0.01
    
for day_num in range(day):																										#For Statement to justify calculate the days
    if day == 0:
        print("Well, I guess you didn't make anything. Maybe you should get some work in.")										#Exit Statement if the person entered zero
    else:    
        print("Day: ", day_num + 1, end=" ")																					#Statement to computer the table
        total += 2 * total
        roundedTotal= "${:,.2f}".format(total)																					#change the output into a monetary formate
        print("the pennies today are:", roundedTotal)  																			#Final Print Statement to be processed in a loop