#Mickey "Wishes he had just bought Mario Kart instead of writing this" Saine
#SDEV 220
# This program is designed to simulate car racing by creating the car in the picture, starting it from left and running it through the track
#04 October 2020

from tkinter import * # Import all definitions from tkinter
   
class Main:																								#Define Main
    def __init__(self):
        window = Tk() 																					# Create a window
        window.title("1-byte Mario Kart by M. Saine II") 												# Set a title
         
        self.width = 1200 																				# Width of self.canvas
        self.canvas = Canvas(window, bg = "#87CEEB", width = self.width, height = 150)

        self.canvas.bind("<Up>", self.faster)															#bind a listener for the "Up button"
        self.canvas.bind("<Down>", self.slower)															#bind a listener for the "Down button"
		
        self.canvas.pack()		

		
        frame = Frame(window)																			#Add a frame into the window
        frame.pack()																					#Pack the Frame
		
        #btFaster = Button(frame, text = "Faster", command = self.faster)                               #buttons commented because I couldn't get the binding to work, but the button did, so it shows the def faster and def slower does work.
        #btFaster.pack(side = LEFT)
        #btSlower = Button(frame, text = "Slower", command = self.slower)
        #btSlower.pack(side = LEFT)
        
        self.x = 10  																					# Starting x position 
        self.sleepTime = 100 																			# Set a sleep time 
		
        self.canvas.create_polygon( 50,50,100,50,125,75,25,75,fill="#8a0d04", tags = "roof")			#Create Roof
        self.canvas.create_line( 50,50,100,50,125,75,25,75,fill="black", tags = "roof1")				#Create Roof outline
        self.canvas.create_rectangle(self.x,75,140,100,fill="#8a0d04", tags = "body")					#Create the Car Body
        self.canvas.create_oval(20,95,45,125,fill="black", tags = "tire")								#Create Rear Tire
        self.canvas.create_oval(105,95,130,125,fill="black", tags = "tire1")							#Create the Front Tire		
        
        self.dx = 5
        self.isStopped = False 
        self.animate()
		
   			
        

        window.mainloop() 																				# Create an event loop
        
   
    def faster(self, event): 																			# Speed up the animation 
        if self.sleepTime > 5:
           self.sleepTime -= 20
                 
    def slower(self, event): 																			# Slow down the animation 
        self.sleepTime += 20
                                  
    def animate(self): 																					# Move the car 
        while not self.isStopped:
            self.canvas.move("roof", self.dx, 0) 														# Move the roof the specified number of dx
            self.canvas.move("roof1", self.dx, 0) 														# Move the roof outline the specified number of dx 
            self.canvas.move("body", self.dx, 0) 														# Move the body the specified number of dx 
            self.canvas.move("tire", self.dx, 0) 														# Move the front tire the specified number of dx
            self.canvas.move("tire1", self.dx, 0) 														# Move the rear tire the specified number of dx			
            self.canvas.after(self.sleepTime) 															# Sleep 
            self.canvas.update() 																		# Update canvas 
            if self.x < self.width:
                self.x += self.dx  																		# Set new position 
            else:
                self.x = 0 																				# Reset string position to beginning
                self.canvas.delete("roof")																#Deletes the old roof for redraw at the beginning
                self.canvas.delete("roof1")																#Deletes the old roof outline for redraw at the beginning 
                self.canvas.delete("body") 																#Deletes the old Car Body for redraw at the beginning
                self.canvas.delete("tire") 																#Deletes the old front tire for redraw at the beginning	
                self.canvas.delete("tire1")																#Deletes the old back tire for redraw at the beginning	 

                
                self.canvas.create_polygon( 50,50,100,50,125,75,25,75,fill="#8a0d04", tags = "roof")     # Redraw roof at the beginning
                self.canvas.create_line( 50,50,100,50,125,75,25,75,fill="black", tags = "roof1")         # Redraw roof outline at the beginning
                self.canvas.create_rectangle(self.x,75,140,100,fill="#8a0d04", tags = "body")            # Redraw Car Body at the beginning
                self.canvas.create_oval(20,95,45,125,fill="black", tags = "tire")                		 # Redraw redraw rear tire at the beginning
                self.canvas.create_oval(105,95,130,125,fill="black", tags = "tire1")                	 # Redraw redraw front tire at the beginning	

			
                                       
Main() 																									#Execution of main class