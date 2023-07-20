import tkinter as tk
from PIL import ImageTk, Image
import csv
import pandas as pd

#define all functions needed here:

#defining the function to get mouse click coords for shot tracking location
mouseClickX = 0
mouseClickY = 0
def getorigin(eventorigin):
    #WARNING DO NOT TRY TO CHANGE THIS VALUE WHILE IT IS BEING CALLED
    global mouseClickX, mouseClickY
    mouseClickX = eventorigin.x
    mouseClickY = eventorigin.y
    #print(mouseClickX,mouseClickY)

#function for reading roster
def readRoster():
    #insert roster name as the file here - add where you can do this in the app []
    global list_of_dict
    with open("./FakeUNCRoster.csv", 'r') as f:
        dict_reader = csv.DictReader(f)
        list_of_dict = list(dict_reader)
        print(list_of_dict)

#filler functions for testing idea
def coordinateSaving():
    print(str(mouseClickX) + ', ' + str(mouseClickY))

#function for creating buttons used for creating buttons for who scored
def createButtonsRoster(window):
    for x in list_of_dict:
        tk.Button(window, text=x['Player']).pack()
        print(x)

#create buttons for the different things to list after rink is pressed
def createVariableButtons(window):
    tk.Button(window, text='Goal', command=coordinateSaving).pack()
    tk.Button(window, text='Shot', command=coordinateSaving).pack()
    tk.Button(window, text='Hit', command=coordinateSaving).pack()
    tk.Button(window, text='Penalty', command=coordinateSaving).pack()

#create a new window function for after rink is pressed
def openRinkWindow():
    #Toplevel object which will be treated as a new window
    newRinkWindow = tk.Toplevel(root)
    #sets the title of the Toplevel widget
    newRinkWindow.title("New Window")
    newRinkWindow.geometry("200x200")
    #use button create function to pack the window on the rink
    createVariableButtons(newRinkWindow)
    #### A Label widget to show in toplevel
    ####tk.Label(newRinkWindow, text ="These are the players on UNC's Hockey Team: " + str(list(map(lambda rec: rec.get('Player'), list_of_dict)))).pack()

#create gui and place objects/buttons
root = tk.Tk()

#roster is read using our script at the beginning of the 
readRoster()
#print(list_of_dict[1]["Player"])

#if mouse button one is clicked log coordinates in console
root.bind("<Button 1>",getorigin)

#define window dimensions
root.geometry("700x500")

#create button with rink image on it
img = ImageTk.PhotoImage(Image.open("./rink.jpg"))
tk.Button(root, text = "Button", image = img, command=openRinkWindow).pack(side = 'top', pady=45)

#ending the program
root.mainloop()