#Mickey "very simple man" Saine
#SDEV 220
# This program is designed to write a function that checks whether a string is a valid password. Suppose the password rules are as follows: A password must have at least 9 characters, consist of only letters and digits, and contain at least two digits.
#20 September 2020



import time

print("Welcome to Iron Man Jack's Password Testing LIFT-A-RAMA...")																						#Provides user with Title
print("version 1.0") 																																	#Provides Version Number
print ("")
time.sleep(1)
print("This program is designed to check whether or not the password you selected meets the appropriate Level of Strength...")							#Provides User with Lay-man definition of issue 
print ("")
time.sleep(1)
print ("")
print ("Patent pending, 2020")
print ("")
time.sleep(1)
password = input("Please enter a password for old Iron Man Jack to life, access and look at: ")

digitNum = 0
charNum = 0


for c in password[:]:
    if c.isdigit():																																			#First we start an if statement that checks is the password has at least one digit
        digitNum += 1
    elif c.isalpha():																																		#Then we pass it through and check to see if it has at least one number
        charNum += 1
    else:
        print("That password is invalid. There's not enough Stuff for it!")																					#If it doesn't meet these criteria, then we break from the loop and ignore the out-loop, to display invalid password
        exit()
        break
if digitNum >= 3 and charNum >= 9:																															#Assuming it met the first criteria and moved to the next loop, we ask the program if there are more than/equal to three digits or whether the string values are greater than/equal to 9 
    print("That password works! I like the way it looks!")																									#Loop finished one way or another, whether validating password or invalidating it.
else:
    print("That password is invalid. There's not enough Stuff for it!")