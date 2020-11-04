#Mickey "not crazy, just proud" Saine
#SDEV 220
# This program is designed to prompts the user to enter an integer from 1 to 15 and displays a pyramid and inverted, as shown in the textbook
#20 September 2020



import time

print ("Greetings. I am the Count.")
print ("")
time.sleep(1)
print ("Yes, The count of Sesame Street...")
print ("")
time.sleep(1)
print (" WELCOME TO...")
print ("")
time.sleep(1)
print (" Wait, Whaaaa...YES, that Seseams Street...")
print ("")
time.sleep(1)
print (" Now, IF you're done...WELCOME TOOOOOOOOOO...")
print ("")
time.sleep(1)
print("The Count's counting Pyramid of Learnability...")																																				#Provides user with Title
print("version 1.0") 																																													#Provides Version Number
print ("")
time.sleep(1)
time.sleep(1)
print ("")
print ("Patent pending, 2020")
print("You enter a number and I turn it into a Pyramid of Glorious, Glorious Numbers......")																													#Provides User with Lay-man definition of issue 
print ("")
time.sleep(1)
number = int (input("So, please enter an Integer from 1 to 15, and allow me to turn it into a Pyramid for you:"))


for i in range(1, number+1):									#Defines Rows of the Pyramid by ranging from 1 to whatever the user selects
    for j in range (11 - i):									#Defines right column spacing
       print (" ", end = " ")
    for j in range (1, i ):										#Provides the left side of column
        print (j, end = " ")
    for i in range (i, 0, -1 ):									#Defines right column w/o spacing
        print (i, end = " ")
		
    print("\n")													#prints a new line
	
for i in range(number, 0, -1):									#Defines Rows of the reverse Pyramid by ranging from 1 to whatever the user selects
    for j in range(11 - i ):									#Define right column spacing
       print (" ", end = " ")
    for j in range (1, i ):										#Provides the left side of column
        print (j, end = " ")
    for i in range (i, 0, -1 ):									#Defines right column w/o spacing
        print (i, end = " ")
		
    print("\n")		