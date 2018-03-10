import Tkinter as tk
import os
import Data
import time

clear = lambda: os.system('cls')
clear()
def filter():
    b = Data.Make_Filters()
    f = open("filters.txt","w")
    for i in range(8):
        f.write(str(b[i])+"\n")
    f.close()
    clear()
    print " Filters added"
def Start_search():
    try:
        filters = []
        f = open("filters.txt","r")
        for l in f:
            filters.append(l)
        if filters != []:
            b = Data.Search(filters)
        f.close()
        f = open("cars.txt","w")
        for i in range(len(b)):
            f.write(str(b[i][0])+"^$@$"+str(b[i][1])+"^$@$"+str(b[i][2])+"^$@$"+str(b[i][3])+"^$@$"+str(b[i][4])+"\n")
        f.close()
        clear()
        print " Got all results"
    except:
        print " Give filters before trying to search"
def Delete_Filters():
    try:
        clear()
        os.remove("filters.txt")
        print " Filters deleted"
    except:
        print " Filters already deleted"

def Delete_Cars():
    try:
        clear()
        os.remove("cars.txt")
        print " Saved cars deleted"
    except:
        print " Saved cars already deleted"

def Show_Filters():
    try:
        clear()
        f = open("filters.txt","r")
        print f.read()
    except:
        print " No filters added"

def Show_Cars():
    try:
        f = open("cars.txt","r")
        b = []
        for l in f:
            b.append(l.split("^$@$"))
        for i in range(len(b)):
            print b[i]
    except:
        clear()
        print " Search at least ones before trying to show cards"
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button1 = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button1.pack(side=tk.LEFT)

button2 = tk.Button(frame,
                   text="Give Filters",
                   command=filter)
button2.pack(side=tk.RIGHT)

button3 = tk.Button(frame,
                    text="Start Searching",
                    command=Start_search)
button3.pack(side=tk.RIGHT)

button4 = tk.Button(frame,
                    text="Delete Filters",
                    command=Delete_Filters)
button4.pack(side=tk.RIGHT)

button5 = tk.Button(frame,
                    text="Show Filters",
                    command=Show_Filters)
button5.pack(side=tk.RIGHT)

button6 = tk.Button(frame,
                    text="Show saved cars",
                    command=Show_Cars)
button6.pack(side=tk.RIGHT)

button6 = tk.Button(frame,
                    text="Delete saved cars",
                    command=Delete_Cars)
button6.pack(side=tk.RIGHT)


root.mainloop()

