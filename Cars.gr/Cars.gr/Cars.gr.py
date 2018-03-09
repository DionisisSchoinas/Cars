import Tkinter as tk
import os

def write_slogan():
    print("Tkinter is easy to use!")
def print1():
	print ("o hi mark")
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
                   command=os.system('python Data.py'))
slogan.pack(side=tk.LEFT)

root.mainloop()

