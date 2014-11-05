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

circle = drawpad.create_oval(10, 10, 40, 40, fill='yellow')
direction = 1

def animate():
    global direction
    x1, y1, x2, y2 = drawpad.coords(circle)
    if x2 > drawpad.winfo_width(): 
        direction = - 5
    elif x1 < 0:
        direction = 5

drawpad.move(circle,direction,0)
drawpad.after(1, animate)
animate()

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
	   
	   drawpad.move(player,0,-20)
		
	def leftClicked(self,event):
	   global oval
	   global player
	   
	   drawpad.move(player,-20,0)	
	   
	def rightClicked(self,event):
	   global oval
	   global player
	   
	   drawpad.move(player,20,0)
	   
	def downClicked(self,event):
	   global oval
	   global player
	   
	   drawpad.move(player,0,20)
	   
	   
	   
app = MyApp(root)
root.mainloop()