#Mickey "Is tired of using pencils to draw shapes" Saine
#SDEV 220
# This program is designed to design a create a program that draws a triangle or diamond. It is also designed to fill those in if the fill mark is checked
#04 October 2020

from tkinter import *


class main:
    def __init__(self):
        window = Tk() 																											# Create a window
        window.title("The Supertabulous Shaper Maker Thingy-ma-bob by M. Saine II")												#Set a Title
        self.v1 = IntVar()																										#sets the variable to tie to buttons for shape determination
        self.v2 = IntVar()																										#sets the variable to tie to buttons for shape determination
		
        self.canvas = Canvas(window, width=800, height=600, bg="#8a0d04")														#set the Canvas in the title
        self.canvas.pack()																										#pack the Canvas on the Window
		
        frame = Frame(window)																									#Places Frame for the bottons
        diamond = Radiobutton(frame, text="Diamond", variable=self.v1, value=1, command=self.draw).grid(row=1, column=1)		#Places a Radio Button for Diamonds in row 1, col 1
        triangle = Radiobutton(frame, text="Triangle", variable=self.v1, value=2, command=self.draw).grid(row=1, column=2)		#Places a Radio Button for Triangles in row 1, col 2
        fillshape = Checkbutton(frame, text="Filled", variable=self.v2).grid(row=1, column=3)									#Places a Check Button for Shaded shapes in row 1, col 3
        frame.pack()

        window.mainloop()

    def draw(self):
        if self.v2.get() == 1:																									#if else statement to check for what shape to draw in shaded
            if self.v1.get() == 1:
                self.canvas.create_polygon(400,30, 600,200,400, 400, 200, 200, 400,30)											#Draws a shaded Triangle through a polygon method
            else:
                self.canvas.create_polygon(400,100, 600,400, 200, 400, 400, 100)												#Draws a Shaded Diamond trhough a polygon method
        else:																													#Further else statement, so if check isn't checked, these are the shapes it draws
            if self.v1.get() == 1:
                self.canvas.create_line(400,30, 600,200,400, 400, 200, 200, 400,30)												#Draws a regular Triangle through the line method
            else:
                self.canvas.create_line(400,100, 600,400, 200, 400, 400, 100)													#Draws a regular Diamond through the line method

main()																															#execution of main class