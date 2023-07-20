import tkinter as tk
from PIL import ImageTk, Image

#define all functions needed here:

#defining the function to get mouse click coords for shot tracking location
mouseClickX = 0
mouseClickY = 0
def getorigin(eventorigin):
      #WARNING DO NOT TRY TO CHANGE THIS VALUE WHILE IT IS BEING CALLED
      global mouseClickX, mouseClickY
      mouseClickX = eventorigin.x
      mouseClickY = eventorigin.y
      print(mouseClickX,mouseClickY)

#create a new window function for after rink is pressed
def openRinkWindow():
    # Toplevel object which will
    # be treated as a new window
    newRinkWindow = tk.Toplevel(root)
    # sets the title of the
    # Toplevel widget
    newRinkWindow.title("New Window")
    # sets the geometry of toplevel
    newRinkWindow.geometry("200x200")
    # A Label widget to show in toplevel
    tk.Label(newRinkWindow, text ="This is a new window").pack()

#create gui and place objects/buttons
root = tk.Tk()

#if mouse button one is clicked log coordinates in console
root.bind("<Button 1>",getorigin)

#define window dimensions
root.geometry("700x500")

#create button with rink image on it
img = ImageTk.PhotoImage(Image.open("./rink.jpg"))
tk.Button(root, text = "Button", image = img, command=openRinkWindow).pack(side = 'top', pady=45)


root.mainloop()