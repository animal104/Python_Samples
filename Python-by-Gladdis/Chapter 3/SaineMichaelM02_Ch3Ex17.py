#Mickey "trys hard to be functional and elegant" Saine
#SDEV 140
# This program is designed to troubleshoot a bad WiFi Connection (rather poorly and with no real "pizazz", but it got designed anyway!
#13 September 2020



import time

print("Welcome to the Magical WiFi repairer stand-in...")																	#Provides user with Title
print("version 1.0") 																										#Provides Version Number
print ("")
time.sleep(1)
print("This program is designed to aid our customers in WiFi trouble shooting...")											#Provides User with Lay-man definition of issue 
print ("")
time.sleep(1)
print ("")
print ("Patent pending, 2020")
print ("")
time.sleep(1)
print ("So let\'s get started with this simple question that we will match with the computer\'s answer...")
print ('')
name= input("What is your first and last name so I can look up your account with us:")										#Shows name on screen, as per Instructor's Requirement
print ("")
time.sleep(1)
print ("Well, ", name, ". Ahh, I see your account right here!", sep="")
print ("")
question0 = input("So,My understanding is that you are having WiFi issues? \nIs this correct? <y=yes/n=No>")				#Beginning input

if question0 == "N" or question0 == "n":																					#answer leads to loop
	print ("Awesome, I'm so glad I could help. \nHave a Wonderful Day!")
else:
	question1 = input("Reboot the computer and try to connect. \nDid that fix the problem? <y=yes/n=No>")
		
	if question1== "Y" or question1== "y":
		print ("Awesome, I'm so glad that I could help you!")
	else:
		question2 = input ("Reboot the router and try to connect. \nDid that fix the problem? <y=yes/n=No>")
		
		if question2== "Y" or question2== "y":
			print ("Awesome, I'm so glad that I could help you!")
		else: 
			question3 = input ("Make sure the cables between the router and modem are plugged in firmly. \nDid that fix the problem? <y=yes/n=No>")
		
			if question3 == "Y" or question3 == "y":
				print ("Awesome, I'm so glad that I could help you!")
			else: 
				question4 = input("Move the router to a new location. \nDid that fix the problem? <y=yes/n=No>")
			
				if question4 == "Y" or question4 == "y":
					print ("Awesome, I'm so glad that I could help you!")
				else: print("Get a new router.")
			

print ("I'm so glad that you issue was resolved in the best way possible. \nHave a Wonderful day!")









