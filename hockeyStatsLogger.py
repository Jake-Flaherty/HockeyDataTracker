import tkinter as tk
from PIL import ImageTk, Image
import csv
import pandas as pd
import os

#define all functions needed here:

#function for reading roster
def readRoster():
    #insert roster name as the file here - add where you can do this in the app []
    global list_of_dict
    with open("./2023FakeUNCRosterStats.csv", 'r') as f:
        dict_reader = csv.DictReader(f)
        list_of_dict = list(dict_reader)
        #print(list_of_dict)


#defining the function to get mouse click coords for shot tracking location
mouseClickX = 0
mouseClickY = 0
def getorigin(eventorigin):
    #WARNING DO NOT TRY TO CHANGE THIS VALUE WHILE IT IS BEING CALLED
    global mouseClickX, mouseClickY
    mouseClickX = eventorigin.x
    mouseClickY = eventorigin.y
    #print(mouseClickX,mouseClickY)

#filler functions for testing idea
def coordinateSaving():
    print(str(mouseClickX) + ', ' + str(mouseClickY))

##defining function to change values in player dictionary
#add a way to write coordinates to a seperate file to look at shot selection []
#add a writer for game by game saving using file naming using datetime []
def addGoal(playerVar, typeVar):
    for x in list_of_dict:
        if x['Player'] == playerVar:
            x['G'] = int(x['G'])
            x['G'] += 1
            x[typeVar] = int(x[typeVar])
            x[typeVar] += 1
            x['S'] = int(x['S'])
            x['S'] += 1
            print(x['G'])
            print(x[typeVar])
    newPlayerWindow.destroy()

#function for adding a shot
def addShot(playerVar):
    for x in list_of_dict:
        if x['Player'] == playerVar:
            x['S'] = int(x['S'])
            x['S'] += 1
            print(x['S'])
    newPlayerWindow.destroy()

#add assist function
def addAssist(playerVar):
    assistCounter = 0
    for x in list_of_dict:
        if x['Player'] == playerVar:
            x['A'] = int(x['A'])
            x['A'] += 1
            print(x['A'])
            assistCounter += 1
    if assistCounter >= 2:
        newPlayerWindow.destroy()

#add hit function
def addHit(playerVar):
    for x in list_of_dict:
        if x['Player'] == playerVar:
            x['H'] = int(x['H'])
            x['H'] += 1
            print(x['H'])
    newPlayerWindow.destroy()

def addPen(playerVar, number):
    for x in list_of_dict:
        if x['Player'] == playerVar:
            x['PEN'] = int(x['PEN'])
            x['PEN'] += 1
            x['PIM'] = int(x['PIM']) + number
            print(x['PEN'])
            print(x['PIM'])

#make the window that shows up with goal window
def whichGoalWindow():
    global whichGoalWindow
    whichGoalWindow = tk.Toplevel(root)
    whichGoalWindow.title("What Type of Goal?")
    whichGoalWindow.geometry("200x200")
    tk.Button(whichGoalWindow, text="EVG", command=lambda typeVar="EVG": createButtonsRosterGoal(typeVar)).pack()
    tk.Button(whichGoalWindow, text="PPG", command=lambda typeVar="PPG": createButtonsRosterGoal(typeVar)).pack()
    tk.Button(whichGoalWindow, text="SHG", command=lambda typeVar="SHG": createButtonsRosterGoal(typeVar)).pack()
    tk.Button(whichGoalWindow, text="OTG", command=lambda typeVar="OTG": createButtonsRosterGoal(typeVar)).pack()

def howManyMins():
    global minsWindow
    minsWindow = tk.Toplevel(root)
    minsWindow.title("How long?")
    minsWindow.geometry("200x200")
    tk.Button(minsWindow, text='2', command=lambda number=2: createButtonsRosterPen(number)).pack()
    tk.Button(minsWindow, text='5', command=lambda number=5: createButtonsRosterPen(number)).pack()
    tk.Button(minsWindow, text='10', command=lambda number=10: createButtonsRosterPen(number)).pack()

#function for creating buttons used for creating buttons for who scored
def createButtonsRosterGoal(typeVar):
    #create new Toplevel Window
    global newPlayerWindow
    newPlayerWindow = tk.Toplevel(root)
    newPlayerWindow.title("Player Choice")
    newPlayerWindow.geometry("200x200")
    for x in list_of_dict:
        playerButtons = tk.Button(newPlayerWindow, text=x['Player'], command=lambda m=x['Player']:[ addGoal(m, typeVar), createButtonsRosterAssist()]).pack()
        print(x)

def createButtonsRosterAssist():
    #create new Toplevel Window
    global newPlayerWindow
    newPlayerWindow = tk.Toplevel(root)
    newPlayerWindow.title("Player Choice")
    newPlayerWindow.geometry("200x200")
    for x in list_of_dict:
        playerButtons = tk.Button(newPlayerWindow, text=x['Player'], command=lambda m=x['Player']: addAssist(m)).pack()
        print(x)

#function for creating players assists
def createButtonsRosterShot():
    #create new Toplevel Window
    global newPlayerWindow
    newPlayerWindow = tk.Toplevel(root)
    newPlayerWindow.title("Player Choice")
    newPlayerWindow.geometry("200x200")
    for x in list_of_dict:
        playerButtons = tk.Button(newPlayerWindow, text=x['Player'], command=lambda m=x['Player']:[ addShot(m)]).pack()
        print(x)

#function for adding hits
def createButtonsRosterHit():
    #create new Toplevel Window
    global newPlayerWindow
    newPlayerWindow = tk.Toplevel(root)
    newPlayerWindow.title("Player Choice")
    newPlayerWindow.geometry("200x200")
    for x in list_of_dict:
        playerButtons = tk.Button(newPlayerWindow, text=x['Player'], command=lambda m=x['Player']:[ addHit(m)]).pack()
        print(x)

def createButtonsRosterPen(number):
    #create new Toplevel Window
    global newPlayerWindow
    newPlayerWindow = tk.Toplevel(root)
    newPlayerWindow.title("Player Choice")
    newPlayerWindow.geometry("200x200")
    for x in list_of_dict:
        playerButtons = tk.Button(newPlayerWindow, text=x['Player'], command=lambda m=x['Player']:[ addPen(m, number)]).pack()
        print(x)

#UNUSED FUNCTION!
#create buttons for the different things to list after rink is pressed
#def createVariableButtons(window):
    #tk.Button(window, text='Goal', command=whichGoalWindow).pack()
    #tk.Button(window, text='Shot', command=createButtonsRoster).pack()
    #tk.Button(window, text='Hit', command=createButtonsRoster).pack()
    #tk.Button(window, text='Penalty', command=createButtonsRoster).pack()

#create a new window function for after rink is pressed
def openRinkWindow():
    #Toplevel object which will be treated as a new window
    global newRinkWindow
    newRinkWindow = tk.Toplevel(root)
    #sets the title of the Toplevel widget
    newRinkWindow.title("New Window")
    newRinkWindow.geometry("200x200")
    #use button create function to pack the window on the rink
    #createVariableButtons(newRinkWindow)
    tk.Button(newRinkWindow, text='Goal', command=whichGoalWindow).pack()
    tk.Button(newRinkWindow, text='Shot', command=createButtonsRosterShot).pack()
    tk.Button(newRinkWindow, text='Hit', command=createButtonsRosterHit).pack()
    tk.Button(newRinkWindow, text='Penalty', command=howManyMins).pack()
    #### A Label widget to show in toplevel
    ####tk.Label(newRinkWindow, text ="These are the players on UNC's Hockey Team: " + str(list(map(lambda rec: rec.get('Player'), list_of_dict)))).pack()

#save button for writing the changes to the csv roster file
def saveAsCSV():
    #final calculations for the file like p/gp and p and s%
    for player in list_of_dict:
        player['P'] = int(player['G']) + int(player['A'])

    for player in list_of_dict:
        if int(player['S']) > 0:
            player['S%'] = int(player['G'])/int(player['S'])
        else:
            player['S%'] = 0

    #write to the file
    CSVdf = pd.DataFrame(list_of_dict)
    CSVdf.to_csv('2023FakeUNCRosterStats.csv', index=False)

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