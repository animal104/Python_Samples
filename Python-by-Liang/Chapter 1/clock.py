#Mickey "getting up and getting coffee" Saine
#SDEV 220
#Write a turtle program that displays a clock to show the time
#06 September 2020


import turtle
import time	

turtle.showturtle()
turtle.setup(900,900)
turtle.bgcolor("black")
turtle.color("yellow")


turtle.write ("Welcome to my AMAZING Clock", move=True, align="center", font=("Arial Black", 25, "normal"))								#Defining the project for the user
time.sleep(2) 
turtle.clear()
turtle.write ("version 1.0", move=True, align="center", font=("Arial Black", 12, "normal"))												#defining the version number
time.sleep(2) 
turtle.clear()
turtle.penup()	
turtle.goto(-350,0)
turtle.pendown()
turtle.write ("This program shows my clock that is ALWAYS set to 6:45:00", move=True, align="left", font=("Arial Black", 16, "normal"))	#Define the purpose to the User
time.sleep(2) 
turtle.clear()
turtle.penup()	
turtle.goto(-200,0)
turtle.pendown()
turtle.write ("C\'mon, you didn't think I wouldn't have SOMETHING TO SAY? It's what I do...", move=True, align="left", font=("Arial Black", 8, "normal"))
time.sleep(2) 
turtle.clear()
turtle.penup()	
turtle.goto(-180,0)
turtle.pendown()
turtle.write ("Let\'s get this started...", move=True, align="center", font=("Arial Black", 16, "normal"))
time.sleep(2)  
turtle.color("White")
turtle.clear()
turtle.hideturtle()
turtle.speed(6)





turtle.penup()					#creation of the circle
turtle.goto(0,-360)
turtle.pendown()
turtle.color("white")	
turtle.begin_fill()				
turtle.fillcolor("white")
turtle.circle(360)
turtle.end_fill()

turtle.color("red")				#making the outside edge
turtle.pensize(10)
turtle.circle(360)


turtle.penup()					#making the second hand
turtle.goto(0,0)
turtle.left(90)
turtle.color("blue")
turtle.pensize(4)
turtle.pendown()
turtle.forward(250)


turtle.penup()					#making the hour hand
turtle.goto(0,0)
turtle.right(180)
turtle.pendown()
turtle.color("black")
turtle.pensize(6)
turtle.forward(225)
turtle.penup()

			
turtle.goto(0,0)				#making the min hand
turtle.right(90)
turtle.pendown()
turtle.forward(300)
turtle.penup()


					
					


				
turtle.goto(0,0)				#Adding the finishing touch
turtle.pensize(10)
turtle.color("red")
turtle.pendown()
turtle.dot()	

turtle.done()					#keeps the Screen open for the instructor to evaluate the results			



