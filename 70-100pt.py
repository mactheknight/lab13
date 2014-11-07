# -*- coding: utf-8 -*-
#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='black')
player = drawpad.create_oval(390,580,410,600, fill="white")

# Create your "enemies" here, before the class

enemy1 = drawpad.create_oval(10, 400, 40, 430, fill='lavender')
direction = 1

enemy2 = drawpad.create_oval(10, 270, 40, 300, fill='lightblue')
direction = 1

enemy3 = drawpad.create_oval(10, 110, 40, 140, fill='pink')
direction = 1

        # Animating the enemies

def animate():
    global direction
    x1, y1, x2, y2 = drawpad.coords(enemy1)
    if x2 > drawpad.winfo_width(): 
        direction = - 5
    elif x1 < 0:
        direction = 5

    drawpad.move(enemy1,direction,0)
    drawpad.after(4, animate)
animate()


def animate2():
    global direction
    x1, y1, x2, y2 = drawpad.coords(enemy2)
    if x2 > drawpad.winfo_width(): 
        direction = - 5
    elif x1 < 0:
        direction = 5
        
    drawpad.move(enemy2,direction,0)
    drawpad.after(20, animate2)
animate2()

        
def animate3():
    global direction
    x1, y1, x2, y2 = drawpad.coords(enemy3)
    if x2 > drawpad.winfo_width(): 
        direction = - 5
    elif x1 < 0:
        direction = 5

    drawpad.move(enemy3,direction,0)
    drawpad.after(15, animate3)
animate3()

        # Creating the buttons

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="△", background= "white")
       	    self.up.grid(row=0,column=2)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    #Left Button
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text=" ⊳ ", background= "white")
       	    self.left.grid(row=2,column=1)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    # Right Button
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text=" ⊲ ", background= "white")
       	    self.right.grid(row=2,column=3)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	   
       	   # Down Button
       	      
       	    self.down = Button(self.myContainer1)     
       	    self.down.configure(text="▽", background= "white")
       	    self.down.grid(row=3, column=2)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    	
	def upClicked(self, event):   
	   global oval
	   global player
	   
	   drawpad.move(player,0,-10)
		
	def leftClicked(self,event):
	   global oval
	   global player
	   
	   drawpad.move(player,-10,0)	
	   
	def rightClicked(self,event):
	   global oval
	   global player
	   
	   drawpad.move(player,10,0)
	   
	def downClicked(self,event):
	   global oval
	   global player
	   
	   drawpad.move(player,0,10)
	  
app = MyApp(root)
root.mainloop()