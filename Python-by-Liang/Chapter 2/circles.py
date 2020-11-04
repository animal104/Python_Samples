#Mickey "Have several boring meetings" Saine
#SDEV 220
#that prompts the user to enter the radius and draws four circles in the center of the screen, as shown in Figure 2.4a 
#06 September 2020

import turtle
import time

turtle.showturtle()
turtle.setup(900,900)
turtle.bgcolor("black")
turtle.color("red")

turtle.write ("Welcome to The Rings of DESTINY", move=True, align="center", font=("Arial Black", 25, "normal"))																#Defining the project for the user
time.sleep(2) 
turtle.clear()
turtle.write ("version 1.0", move=True, align="center", font=("Arial Black", 12, "normal"))																					#Provides Version Number
time.sleep(2) 
turtle.clear()
turtle.penup()	
turtle.goto(-350,0)
turtle.pendown()
turtle.write ("This program improves my clock by making six distinct circles to build clocks from...", move=True, align="left", font=("Arial Black", 8, "normal"))			#Define the purpose to the User
time.sleep(2) 
turtle.clear()
turtle.penup()	
turtle.goto(-200,0)
turtle.pendown()
turtle.write ("This would be a lot funner if the directions didn\'t say to match figure 2.4a...", move=True, align="left", font=("Arial Black", 8, "normal"))
time.sleep(2) 
turtle.clear()
turtle.penup()	
turtle.goto(-180,0)
turtle.pendown()
turtle.write ("Let\'s get this started...", move=True, align="center", font=("Arial Black", 16, "normal"))
time.sleep(2)  
turtle.color("black")
turtle.clear()
turtle.bgcolor("white")									#resetting the page to match the figure
turtle.hideturtle()



radius = eval(input("Enter the desired radius for the six circles you wish to see drawn on the screen: "))


turtle.pendown()


turtle.circle(radius)									#creating circle 1
turtle.penup()

turtle.forward(radius*2)								#creating circle 2
turtle.pendown()
turtle.circle(radius)
turtle.penup() 

turtle.forward(radius*2)								#creating circle 3
turtle.pendown()
turtle.circle(radius)
 

turtle.right(180)										#creating circle6
turtle.circle(radius)
turtle.penup() 

turtle.forward(radius*2)								#creating circle 5
turtle.pendown()
turtle.circle(radius)
turtle.penup() 

turtle.forward(radius*2)								#creating circle 4
turtle.pendown()
turtle.circle(radius)

turtle.done()											#keeps the Screen open for the instructor to evaluate the results		


