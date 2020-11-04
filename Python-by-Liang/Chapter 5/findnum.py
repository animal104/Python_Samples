#Mickey "nerd-core forever!" Saine
#SDEV 220
# This program is designed to display, ten numbers per line, all the numbers from 200 to 400 that are divisible by 7, but not 8. The numbers are separated by exactly one space.
#20 September 2020



import time

print("Welcome to the Divisibility table of D-0-0-M...")																											#Provides user with Title
print("version 1.0") 																																				#Provides Version Number
print ("")
time.sleep(1)
print("This program is designed to display all the numbers divisble by 7, BUT NOT 8, from 200-400...")																#Provides User with Lay-man definition of issue 
print ("")
time.sleep(1)
print ("")
print("Why Eight?!?! I dunno why?? Eight really did something offensive and was canceled on Twitter last week, so we don't speak that name...")																
print ("")
time.sleep(1)
print ("")
print ("Patent pending, 2020")
print ("")
time.sleep(1)
print ("Watch and Behold. See and Peer. We will take the range of numbers from 200 - 400, and see if they are divisble by 7, BUT not 8.")							#instead of asking for input, THIS program declares it's intentions
print ("")
time.sleep(1)
print ("Then, these amazing and beautiful numbers will arrange themselves in rows of 10s and magically spaced by 1")
print ("")
time.sleep(1)

count = 1																																							#declares count at 1
for number in range(200, 401):																																		#for statement to feed a range to the attached if statment
    if number % 7 == 0 and number % 8 !=0:																															#If statment to determine if numbers are divisable by 7 but not 8
        if count % 10 != 0:																																			#nested if statement to break the numbers into lines
            print(number, end = " ")
        else:
            print(number)    
        
        count += 1																																					#count advancer for the number of int per line
		
print ("")
print ("")
time.sleep(1)
print ("...and now you see the wonders of the D-0-0-M Mind!")
print ("")
time.sleep(1)
print ("Behold and Despair!")																																		#final friendly greeting that expresses my love for the world