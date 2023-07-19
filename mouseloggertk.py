import tkinter as tk
from PIL import ImageTk, Image

#define all functions needed here
mouseClickX = 0
mouseClickY = 0
#defining the function to get mouse click coords for shot tracking location
def getorigin(eventorigin):
      #WARNING DO NOT TRY TO CHANGE THIS VALUE WHILE IT IS BEING CALLED
      global mouseClickX, mouseClickY
      mouseClickX = eventorigin.x
      mouseClickY = eventorigin.y
      print(mouseClickX,mouseClickY)

#note to self this works

#create gui and place objects/buttons
root = tk.Tk()
#if mouse button one is clicked log coordinates in console
root.bind("<Button 1>",getorigin)
#define window dimensions
root.geometry("700x500")
#define the frame in the root window
frame = tk.Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.35)
img = ImageTk.PhotoImage(Image.open("./rink.jpg"))
#create a Label Widget to display the text or Image
label = tk.Label(frame, image = img)
label.pack()



root.mainloop()