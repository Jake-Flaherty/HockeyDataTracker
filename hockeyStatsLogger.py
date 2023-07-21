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


##defining function to change values in player dictionary

#add a way to write coordinates to a seperate file to look at shot selection []
#add a writer for game by game saving using file naming using datetime []
def addGoal(playerVar):
    for x in list_of_dict:
        if x['Player'] == playerVar:
            x['Goals'] = int(x['Goals'])
            x['Goals'] += 1
            print(x['Goals'])


#function for creating buttons used for creating buttons for who scored
def createButtonsRoster():
    #create new Toplevel Window
    newPlayerWindow = tk.Toplevel(root)
    newPlayerWindow.title("Player Choice")
    newPlayerWindow.geometry("200x200")
    for x in list_of_dict:
        playerButtons = tk.Button(newPlayerWindow, text=x['Player'], command=lambda m=x['Player']: addGoal(m)).pack()
        print(x)

#create buttons for the different things to list after rink is pressed
def createVariableButtons(window):
    tk.Button(window, text='Goal', command=createButtonsRoster).pack()
    tk.Button(window, text='Shot', command=createButtonsRoster).pack()
    tk.Button(window, text='Hit', command=createButtonsRoster).pack()
    tk.Button(window, text='Penalty', command=createButtonsRoster).pack()

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

#save button for writing the changes to the csv roster file
def saveAsCSV():
    CSVdf = pd.DataFrame(list_of_dict)
    CSVdf.to_csv('FakeUNCRoster.csv', index=False)

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
saveButton = tk.Button(root, text='SAVE', fg='white', bg='blue', command=saveAsCSV).pack(side='bottom')

#ending the program
root.mainloop()