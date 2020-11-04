#Mickey "Have several boring meetings" Saine
#SDEV 140
# This program is designed to determine the percentage of discount, price, and total price of software sales
#13 September 2020



import time

print("Welcome to the Dunder Mifflin's Software Division Discount shopping shoporama...")																#Provides user with Title
print("version 1.0") 																										#Provides Version Number
print ("")
time.sleep(1)
print("This program is designed to help us create an estimate for your software needs...")		#Provides User with Lay-man definition of issue 
print ("")
time.sleep(1)
print ("")
print ("Patent pending, 2020")
print ("")
time.sleep(1)
print ("Well, Good morning!. Welcome to Dunder Mifflin Software Sales. My name is Dwight, and I'd be happy to help you!", sep="")
print ("")
print ("So let\'s get started with this simple question...")
print ("")
name= input("What is your first and last name to ensure this paperwork is appropriately filled out:")														#Shows name on screen, as per Instructor's Requirement
print ("")
time.sleep(1)
print ("Well, ", name, ", I'll assume that you are calling about one of our fine software packages at retail for $99.00, but I might be able to do a little better depending on how much you order.", sep="")
print ("")
time.sleep(1)
print ("If you buy 10-15, we can offer a 10% discount")
print ("")
time.sleep(1)
print ("If you buy 20-49, we can offer a 20% discount")
print ("")
time.sleep(1)
print ("If you buy 50-99, we can offer a 30% discount")
print ("")
time.sleep(1)
print ("If you buy 100 or more, we can offer a 40% discount")
print ("")
time.sleep(2)
package=float(input('So, " name "How many Packages would you like to buy?'))
price = float(99)
print ("")
print ("")
time.sleep(1)
print ("Not bad! Not bad! Let\'s see what we can do for you on pricing.")
print ('')
print ('')
time.sleep(1)
print ("Applying your potential discount")
print ('')
print ('')
time.sleep(1)


if package >=10 and package <= 19:
		price1 = price*.9	
		final_Price1= "${:,.2f}".format(price1)
		package_Sum1 = price1 * package	
		final_Package_Price1= "${:,.2f}".format(package_Sum1)
		print("Good choice! We can offer you a discount that equals to ", final_Price1, ". I think that's a really good deal. We can get you a total price of ", final_Package_Price1, ".", sep="")
	
elif package >=20 and package <= 49:
		price2 = price*.8
		final_Price2= "${:,.2f}".format(price2)
		package_Sum2 = price2 * package	
		final_Package_Price2= "${:,.2f}".format(package_Sum2)
		print("Excellent choice! We can offer you a discount that equals to ", final_Price2, " per package. I think that's a a really great deal. We can get you a total price of ", final_Package_Price2, ".", sep="")
	 		

elif package >=50 and package <= 99:
		price3 = price*.7
		final_Price3= "${:,.2f}".format(price3)
		package_Sum3 = price3* package	
		final_Package_Price3= "${:,.2f}".format(package_Sum3)
		print("Awe-inspiring choice! We can offer you a discount that equals to ", final_Price3, ". I think that's a a really inspired deal. We can get you a total price of ", final_Package_Price3, ".", sep="")
	
elif package >=100:
		price4 = price*.6	
		final_Price4= "${:,.2f}".format(price4)
		package_Sum4 = price4* package
		final_Package_Price4= "${:,.2f}".format(package_Sum4)
		print("yes! Yes! In your face, Jim! I mean, ummm, We can offer you a discount that equals to ", final_Price4, ". I think that's a a really great deal. We can get you a total price of ", final_Package_Price4, ".", sep="")
	
else:
	package_Sum5 = package * 99
	final_Package_Price5= "${:,.2f}".format(package_Sum5)
	print("I'm so sorry. We can definitely sell you software, but I can't apply a discount here. My \"Manager\", Jim, would hold it over my head forever! Your total would be ", final_Package_Price5, ".", sep="")

print ('')
print ('')
time.sleep(1)
print("Do we have a deal here,", name)