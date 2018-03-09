import Tkinter as tk
import os
import Data

clear = lambda: os.system('cls')
clear()
filters = []
def filter():
    b = Data.Make_Filters()
    for i in range(8):
        filters.append(b[i])
def Start_search():
    if filters != []:
        Data.Search(filters)
    else:
        print " Give filters before trying to search"
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

root.mainloop()

