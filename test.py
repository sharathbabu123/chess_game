from tkinter import * 
from tkinter.ttk import *
  
# creating tkinter window
root = Tk()
  
# Adding widgets to the root window
# Label(root, text = 'GeeksforGeeks', font =(
#   'Verdana', 15)).pack(side = TOP, pady = 10)
  
# Creating a photoimage object to use image
photo = PhotoImage(file = r"C:/Users/shara/Desktop/Bored/August 2023/chess_game/assets/black_rook.png")
  
# here, image option is used to
# set image on button
b = Button(root, text = 'Click Me !', image = photo)
b.grid(row=0,column=0)
b.config(text='hi')


mainloop()