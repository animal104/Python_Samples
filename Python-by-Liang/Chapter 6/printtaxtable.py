#Mickey "This program made me reconsider my enthusiasm for Programming" Saine
#SDEV 220
# This program is designed to use the def computerTax (status, taxableIncome) function to write a program that prints a tax table for taxable income from $50,000 to $60,000 with intervals of $50 for all four statuses
#20 September 2020



import time
import sys
import random



def computeTax(status, taxableIncome):																																						#create function based on textbook requirements to calculate tax
    if status == 0:
        if taxableIncome <= 8350:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 33950:
            tax = 8350 * 0.10 + (taxableIncome - 8350) * 0.15
        elif taxableIncome <= 82250:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (taxableIncome - 33950) * 0.25
        elif taxableIncome <= 171550:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (taxableIncome - 82250) * 0.28
        elif taxableIncome <= 372950:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + (taxableIncome - 171550) * 0.33
        else:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + (372950 - 171550) * 0.33 + (taxableIncome - 372950) * 0.35;
		
    elif status == 1:  																																										# Compute tax for Married Jointly filers 
        if taxableIncome <= 16700:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 16700:
            tax = 8350 * 0.10 + (taxableIncome - 16700) * 0.15
        elif taxableIncome <= 82250:
            tax = 8350 * 0.10 + (67950 - 16700) * 0.15 + (137051 - 67904) * 0.25
        elif taxableIncome <= 171550:
            tax = 8350 * 0.10 + (67950 - 16700) * 0.15 + (137051 - 67904) * 0.25 + (208850 - 137051) * 0.28
        elif taxableIncome <= 372950:
            tax = 8350 * 0.10 + (67950 - 16700) * 0.15 + (137051 - 67904) * 0.25 + (208850 - 137051) * 0.28 + (372950 - 208851) * 0.33
        else:
            tax = 8350 * 0.10 + (67950 - 16700) * 0.15 + (137051 - 67904) * 0.25 + (208850 - 137051) * 0.28 + (372950 - 208851) * 0.33 + (taxableIncome - 372950) * 0.35;	
			
    elif status == 2:  																																										# Compute tax for Married Filing Separately filers 
        if taxableIncome <= 8350:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 33950:
            tax = 8350 * 0.10 + (taxableIncome - 8350) * 0.15
        elif taxableIncome <= 82250:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25
        elif taxableIncome <= 171550:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (104425 - 68526) * 0.28
        elif taxableIncome <= 372950:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (104425 - 68526) * 0.28 + (186475 - 68526) * 0.33
        else:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (104425 - 68526) * 0.28 + (186475 - 68526) * 0.33 + (taxableIncome - 186476) * 0.35;		

    elif status == 3:  																																										# Compute tax for Head of Household filers 
        if taxableIncome <= 11950:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 11950:
            tax = 11950 * 0.10 + (taxableIncome - 8350) * 0.15
        elif taxableIncome <= 82250:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (taxableIncome - 33950) * 0.25
        elif taxableIncome <= 171550:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (taxableIncome - 82250) * 0.28
        elif taxableIncome <= 372950:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + (taxableIncome - 171550) * 0.33
        else:
            tax = 8350 * 0.10 + (45500 - 11951) * 0.15 + (117450 - 45501) * 0.25 + (190200 - 117451) * 0.28 + (372950 - 190201) * 0.33 + (taxableIncome - 372951) * 0.35;			
    else:
        print("Error: invalid status")
        sys.exit()


    return(format(tax, ".2f"))	

def quote ():
    quote = random.randint (0,10)																																							#creates a function to randomly assign an ending quote for my amusement, since I have to stare at this problem for over 17 hours
    if quote == 0:
        print ("I saw Wedding Crashers accidentally. I bought a ticket for Grizzly Man and went into the wrong theater. After an hour, I figured I was in the wrong theater, but I kept waiting. Cuz that is the thing about bear attacks… they come when you least expect it.")
    elif quote == 1:
        print ("In an ideal world, I would have all 10 fingers on my left hand so my right hand could just be a fist for punching.")
    elif quote == 2:
        print ("Now that I own the building I’m looking for new sources of revenue. And a daycare center? Muahahahahahahahaha…Well I guess it’s not an evil idea, it’s just a regular idea, but there’s no good laugh for a regular idea.")
    elif quote == 3:
        print ("It’s never the person who you most suspect. It’s also never the person you least suspect since anyone with half a brain would suspect them the most. Therefore, I know the killer to be Phyllis… The person who I most medium suspect.")
    elif quote == 4:
        print ("No, don’t call me a hero. Do you know who the real heroes are? The guys who wake up every morning and go into their normal jobs, and get a distress call from the Commissioner and take off their glasses and change into capes and fly around fighting crime. Those are the real heroes.")
    elif quote == 5:
        print ("No, don’t call me a hero. Do you know who the real heroes are? The guys who wake up every morning and go into their normal jobs, and get a distress call from the Commissioner and take off their glasses and change into capes and fly around fighting crime. Those are the real heroes.")
    elif quote == 6:
        print ("Security in this office park is a joke. Last year I came to work with my spud-gun in a duffel bag. I sat at my desk all day with a rifle that shoots potatoes at 60 pounds per square inch. Can you imagine if I was deranged?")
    elif quote == 7:
        print ("I come from a long line of fighters. My maternal grandfather was the toughest guy I ever knew. World War II veteran, killed twenty men, and spent the rest of the war in an Allied prison camp. My father battled blood pressure and obesity all his life. Different kind of fight.")
    elif quote == 8:
        print ("And I did not become a Lackawanna County volunteer sheriff’s deputy to make friends. And by the way, I haven’t.")
    else:
        print ("I signed up for Second Life about a year ago. Back then, my life was so great that I literally wanted a second one. Absolutely everything was the same…except I could fly.")	
		
print("Welcome to the Dwight Schrute's Official Tax-a-rama Tax tabling effort...")																											#Provides user with Title
print("version 1.0") 																																										#Provides Version Number
print ("")
time.sleep(1)
print("Here at Schrute Farm's, we don't just grow Beets, we also understand your need to understand taxations...")																			#Provides User with set-up of scenerio
print ("")
time.sleep(1)
print("We also provide Taxation Tables that anyone could find in Google, but not as home-made as this...")																					#Provides User with Lay-man definition of issue 
print ("")
time.sleep(1)
print ("")
print ("Patent pending, 2020")
print ("")
time.sleep(1)
print ("Would you like to know the exact rate of the 50,000 dollar range of taxes, as per the 2009 income tax which was demanded in the 15 exercise of this chapter?")
print ("")
print ("Good! So where we go!")
print ("")
time.sleep(1)
print ("Taxable",	"    Single", "\t", "Married", "        Married", "        Head of")																									#Add Header to Table
print ("Income", "\t ", "\t", "\t", "Separate", "       Joint", "\t ", "\t", "a House")
print ("---------------------------------------------------------------------")
for row in range(50000, 60100, 100):																																						#create Row with Tax information
    print(row, "\t   ", computeTax(0, row), "\t", computeTax(1, row),
          "\t", computeTax(2, row), "\t", computeTax(3, row))
	
print ("")																																													#finished the scenario
print("")
print("")
time.sleep(1)
print ("Is there anything else I can help you with, today")
print ("")
time.sleep(1)
print ("Well awesome! We, at Scrute farms, are so excited to be able to meet your needs.")
print ("")
time.sleep(1)
print("Just one last pearl of wisdom that I've been pondering all day...")
print ("")
print (quote())																																												#invokes a function that I temporarily became obsessed with before it was discarded
	
