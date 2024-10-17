from tkinter import *
from tkinter import ttk

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
frame2.grid(row=0, column=1, sticky="nsew")  # Top-right
frame3.grid(row=1, column=0, sticky="nsew")  # Bottom-left
frame4.grid(row=1, column=1, sticky="nsew")  # Bottom-right

# Configure the grid so that rows and columns are of equal size
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


#items in frames-------

#frame1
ttk.Label(frame1, text="Camera View Frame").grid(column=0, row=0)

#frame2
ttk.Label(frame2, text="Buttons Frame").grid(column=0, row=0)

#frame3
ttk.Label(frame3, text="Camera Manager Frame").grid(column=0, row=0)

#frame4
ttk.Label(frame4, text="Data Export Frame").grid(column=0, row=0)




root.mainloop()