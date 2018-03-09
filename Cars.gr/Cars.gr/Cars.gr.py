import Tkinter as tk
import os

def write_slogan():
    print("Tkinter is easy to use!")
def call():
	os.system('python Data.py')
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Search",
                   command=call)
slogan.pack(side=tk.LEFT)

root.mainloop()

