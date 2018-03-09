import Tkinter as tk
import os
import Data

filters = []
def filter():
    filters = Data.Make_Filters()
    print filters
def Start_search():
    print filters
    Data.Search(filters)
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

