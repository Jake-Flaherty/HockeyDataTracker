import tkinter as tk
from PIL import ImageTk, Image
import csv
import pandas as pd
import os

#defining variables 

mouseClickX = 0
mouseClickY = 0

#defining functions 

def readRoster():
    #insert roster name as the file here - add where you can do this in the app []
    global list_of_dict
    with open("./2023FakeUNCRosterStats.csv", 'r') as f:
        dict_reader = csv.DictReader(f)
        list_of_dict = list(dict_reader)
        #print(list_of_dict)

def getorigin(eventorigin):
    #WARNING DO NOT TRY TO CHANGE THIS VALUE WHILE IT IS BEING CALLED
    global mouseClickX, mouseClickY
    mouseClickX = eventorigin.x
    mouseClickY = eventorigin.y

def buttonCoords():
    global trueClickX, trueClickY
    trueClickX = mouseClickX
    trueClickY = mouseClickY
    #print('mhm')

def createPlayers():
    counterY = 25
    for player in list_of_dict:
        tk.Button(root, text = player['Player']).place(bordermode='outside', y=counterY, x = 20)
        counterY += 25

root = tk.Tk()
#define window dimensions
root.geometry("600x400")
root.state("zoomed")
#bind button to things
root.bind("<Button 1>",getorigin)

#functions used to build buttons/gui
readRoster()
createPlayers()

#create button with rink image on it
img = ImageTk.PhotoImage(Image.open("./rink.jpg"))
tk.Button(root, text = "Button", image = img, command = buttonCoords).pack(side = 'right', padx=45)
#saveButton = tk.Button(root, text='SAVE', fg='white', bg='blue', command=saveAsCSV).pack(side='bottom')


#ending the program
root.mainloop()
