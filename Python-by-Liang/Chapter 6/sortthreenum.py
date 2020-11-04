#Mickey "Chooses Star Trek over Star Wars every time" Saine
#SDEV 220
# This program is designed to prompts the user to enter three numbers and invokes the function to display them in increasing and decreasing order
#20 September 2020



import time																																				#class defined to help me see it as a process, even though I know it's a fake calculation

def displaySortedNumbers(num1, num2, num3):																												#This defines the first Function
    if num1 > num2:																																		#This series of "IF" statements sorts the numbers
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2
    print ("The Ascending sorted numbers are ", num1, ", ", num2, ", ", num3, ".", sep="")
	
def displaySortedNumbers2(num1, num2, num3):																											#This second function addresses the additional additions that always throw a kink into my day
    if num1 < num2:																																		#This series of "IF" statements re-sorts the numbers
        num1, num2 = num2, num1
    if num1 < num3:
        num1, num3 = num3, num1
    if num2 < num3:
        num2, num3 = num3, num2
    print ("The descending sorted numbers are ", num1, ", ", num2, ", ", num3, ".", sep="")
	
def main():																																				#The third function is used to tie the other two functions into main, prepare the prints statements
    num1,num2,num3 = eval (input("Enter three numbers: "))																								#and ask my questions, and prepare the testing
    displaySortedNumbers(num1, num2, num3)  
    displaySortedNumbers2(num1, num2, num3)	
     	

print("Welcome to the Number Twister, Re-orderer, and Re-arranger...")																					#Provides user with Title
print("version 1.0") 																																	#Provides Version Number, but today I learned it's okay to release beta 2 before beta 1 according to apple
print ("")
time.sleep(1)
print("This program is designed to take your favorite three numbers and display them in increasing and decreasing order...")							#Provides User with Lay-man definition of issue 
print ("")
time.sleep(1)
print ("")
print ("Patent pending, 2020")
print ("")
time.sleep(1)
print ("Well, There is a specific output that I need to match here, so I guess we gotta get to it.")													#this part whines a lot about my feelings of anxiety concerning the stringent guidelines
print ("")
time.sleep(1)
print ("BUT, isn't it kinda limiting when I have to ask a specific question and get a specific response? There's no Piazzaz in that!")
print ("")
time.sleep(1)
print ("Sigh, I know..Get to it! Here goes...")
print ("")
time.sleep(1)


    


main()																																					#this calls the function, which I could have done without the third function, but making the test a function allows
																																						# a more module feel to it