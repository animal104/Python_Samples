#Mickey "likes shapes and colors as much as Elmo" Saine
#SDEV 220
# This program is designed to demonstrate a class named Triangle that extends the Geometric Object and meets multiple guidelines
#18 October 2020


import time																																					#import time for my witty intro
import datetime																																				#import date-time because that whole Linux mathematical stuff was silly and I like this one better
import math																																					#imports math to help with the mathematical calculations

def intro():																																				#Create my first function to provide my typical witty introductions
    print('''\t \t   Welcome to the  Triangle of YOUR LIFE!!! ''')																							#Provides user with Title
    print('''\t \t \t \t Version 1.0''') 
    today =datetime.datetime.today()	
    date_Written = datetime.date (2020, 10, 18)																												#Provides the time because I learned about it in a video today, and REALLY liked it, so I included it in my witty intro
    print (f'''\t \t \t Patent Pending,{date_Written: %B %d, %Y}''')																						#Changed the Patent Pending to Reflect this newly learned concept of time
    print (''' ''')
    time.sleep(1)
    print('''This program is designed to take some input and create the Triangle that you've always dreamed of.''')											#Provides User with Lay-man definition of issue 
    print (''' ''')
    time.sleep(1)
    print(f'''You are accessing this program at {today:%H:%M, on %A, %B %d, %Y}''')																			#Really just enjoying the time, and want to capture this for later programs
    print (''' ''')
    time.sleep(1)
	
class GeometricObject:																																		#creates geometricObject Super class
    def __init__(self, color='red', filled=True):
        self.__color = color
        self.__filled = filled

    def getColor(self):																																		#defines the attribute of color that will be returned to self. This will be passed to the child class of Triangle.
        return self.__color																																	#Returns the color

    def setColor(self, color):																																#Draws the attribute o color that will be returned to self. This will be passed to the child class of Triangle.
        self.__color = color																																#Sets the color

    def isFilled(self):																																		#defines the attribute of fill that will be returned to self. This will be passed to the child class of Triangle.
        return self.__filled																																#Returns the fill

    def setFilled(self, filled):																															#defines the attribute for set the fill that will be returned to self. This will be passed to the child class of Triangle.
        self.__filled = filled																																#sets the fill

    def __str__(self):																																		#defines the return statement from the self color and self fill that will be given later from the stored information.
        return '''the color of that triangle was ''' + self.__color + ''', and I marked ''' + str(self.__filled) + ''' for the fill on the triangle.'''


class Triangle(GeometricObject):																															#Define the Triangle subclass using attributes from the Geometric class such as color and fill. 
    def __init__(self, side1=2.0, side2=2.0, side3=2.0, color='red', isFilld=True):
        super().__init__(color, isFilld)																													#Shows the attributes (color and fill) that are inherited
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getSide1(self):																																		#Defines the attribute of Side 1
        return self.side1																																	#Returns side 1

    def setSide1(self, side1):
        self.side1 = side1																																	#sets side 1

    def getSide2(self):																																		#Defines the attribute of Side 2
        return self.side2																																	#Defines the attribute of Side 2

    def setSide2(self, side2):
        self.side1 = side2																																	#sets side 2

    def getSide3(self):																																		#Defines the attribute of Side 3
        return self.side3																																	#Defines the attribute of Side 3

    def setSide3(self, side3):
        self.side3 = side3																																	#sets side 3

    def getArea(self):																																		#Defines the Area
        s = (self.side1 + self.side2 + self.side3) / 2																										#Lots of Math
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))																		#More Mathematical Formulas
        return area																																			#Returns the area from the mathematical formulas

    def getPerimeter(self):																																	#Defines the Perimeter
        return self.side1 + self.side2 + self.side3																											#Assigns and returns the math

    def __str__(self):
        return super().__str__() + ''' The first side is ''' + str(self.side1) + ''', and the second side equals ''' + \									#Returns the super string with the answer requested
               str(self.side2) + ''', and the final side is ''' + str(self.side3)


def main():
    intro()
    print(f'''Now breathe! Close your eyes! Imagine that puuurrrrrfect little triangle in the sky''')
    print('''''')
    time.sleep(1)
    print(f'''Okay? Got it?''')
    print(''' ''')
    time.sleep(1)
    s1, s2, s3 = eval(input('''Now tell me about it! Enter in the three sides of the triangle with commas separating them (CSV'd, if you will!): '''))			#input to get the sides of the triangle
    print (''' ''')
    color = input('''Now, enter the color of the triangle that you are imagining!: ''')																			#input to get the color of the triangle
    print (''' ''')
    isFilled = bool(eval(input('''Is this perfect little triangle filled? (<1> for filled or <0> for empty): ''')))												#input to get whether the triangle is filled or not

    triangle = Triangle(s1, s2, s3, color, isFilled)																											#Takes the input listed from the questions and ties it to the Triangle 
	
    print(''' ''')
    print(f'''Well, I think I got that all down. You said that {triangle}''')																					#returns the information from the list created
    print(''' ''')
    time.sleep(1)
    print(f''' Wow! When measuring that I found out that that special triangle's area is {triangle.getArea()}''')												#Returns the area from the Triangle class										
    print (''' ''')	
    time.sleep(1)
    print(f''' For further news, that special little triangle's perimeter is {triangle.getPerimeter()}''')														#Returns the Perimeter from the Triangle



main()																																							#executes the main function