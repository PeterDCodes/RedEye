from tkinter import *
from tkinter import ttk
import sys

#initialize application
root = Tk()
root.title('RedEye')


#create a frame widgets
frame1 = ttk.Frame(root, padding=10)
frame2 = ttk.Frame(root, padding=10)
frame3 = ttk.Frame(root, padding=10)
frame4 = ttk.Frame(root, padding=10)


# Place the frames in a 2x2 grid
frame1.grid(row=0, column=0, sticky="nsew")  # Top-left
frame2.grid(row=0, column=1, sticky="ns")  # Top-right   #ns = north south. nsew means the frame will fill expand in all directions
frame3.grid(row=1, column=0, sticky="nsew")  # Bottom-left
frame4.grid(row=1, column=1, sticky="ns")  # Bottom-right

# Configure the grid so that rows and columns are of equal size
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


#items in frames-------

#frame1
ttk.Label(frame1, text="Camera View Frame").grid(column=0, row=0)


#frame2
ttk.Label(frame2, text="Activate").grid(column=0, row=0)
ttk.Label(frame2, text="Station Name").grid(column=1, row=0)

ttk.Button(frame2, text='Button1', command=root.destroy).grid(column=0,row=1)
ttk.Entry(frame2).grid(column=1,row=1)

ttk.Button(frame2, text='Button2', command=root.destroy).grid(column=0, row=2)
ttk.Entry(frame2).grid(column=1,row=2)

ttk.Button(frame2, text='Button3', command=root.destroy).grid(column=0, row=3)
ttk.Entry(frame2).grid(column=1,row=3)

ttk.Button(frame2, text='Button4', command=root.destroy).grid(column=0, row=4)
ttk.Entry(frame2).grid(column=1,row=4)



#frame3
ttk.Label(frame3, text="Camera Manager Frame").grid(column=0, row=0)
ttk.Button(frame3, text="Camera Config Button").grid(column=0, row=1)



#frame4
ttk.Label(frame4, text="Data Export Frame").grid(column=0, row=0)
ttk.Button(frame4, text="Export as .csv").grid(column=0, row=1)




root.mainloop()