from tkinter import *
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading

#initialize application
root = Tk()
root.title('RedEye')

#styles of the application (This is like a .CSS file)
style = ttk.Style()
style.theme_use('aqua')
style.configure("Custom.TButton", foreground = "white", background="black", borderwidth=0) 


#create root frame widgets
frame1 = ttk.Frame(root, padding=10, border=5, relief="solid")
frame2 = ttk.Frame(root, padding=10, border=5, relief="solid")
frame3 = ttk.Frame(root, padding=10, border=5, relief="solid")
frame4 = ttk.Frame(root, padding=10, border=5, relief="solid")

# Place the frames in a 2x2 grid
frame1.grid(row=0, column=0, sticky="nsew")  # Top-left
frame2.grid(row=0, column=1, sticky="nsew")  # Top-right   #ns = north south. nsew means the frame will fill expand in all directions
frame3.grid(row=1, column=0, sticky="nsew")  # Bottom-left
frame4.grid(row=1, column=1, sticky="nsew")  # Bottom-right

# Configure the grid. the weight determines size of rows and columns
root.grid_rowconfigure(0, weight=4)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=4)
root.grid_columnconfigure(1, weight=1)


#------items in frames-------

#frame1
ttk.Label(frame1, text="Camera View Frame").grid(column=0, row=0)


#frame2
#create sub-frames within frame2
frame2A = ttk.Frame(frame2, padding = 10, border=5, relief="solid")
frame2B = ttk.Frame(frame2, padding = 10, border=5, relief="solid")

#place sub-frames within frame2
frame2A.grid(row=0, column=0, sticky="nsew")  # Top-left
frame2B.grid(row=1, column=0, sticky="nsew")  # Top-right

#column titles
ttk.Label(frame2A, text="Activate").grid(column=0, row=0)
ttk.Label(frame2A, text="Area Name").grid(column=1, row=0)

#list of buttons and entrys in frame 2. uses loop to add all the items
button_count = 10 #will use this based on number of areas of interest allowed. Max 10??
for i in range(button_count):
    ttk.Button(frame2A, text=f'Button{i + 1}', command=root.destroy, style="Custom.TButton").grid(column=0,row=i+1) #row is i+1 because title is at position 0 
    ttk.Entry(frame2A).grid(column=1,row=i+1)


#class selection box in frame 2
ttk.Label(frame2B, text='Class Selection').grid(column=0, row=0, columnspan=2)
#use a loop to add checkboxed based on list of objects
objects = ['class1', 'class2', 'class3', 'class4', 'class5']  #temporary list of classes will want to pull from vision model list of classes
for i, object in enumerate(objects):
    ttk.Checkbutton(frame2B, text = object). grid(column = 0, row = i+1)


#frame3
ttk.Label(frame3, text="Camera Manager Frame").grid(column=0, row=0)
ttk.Button(frame3, text="Camera Config Button").grid(column=0, row=1)


#frame4
ttk.Label(frame4, text="Data Export Frame").grid(column=0, row=0)
ttk.Button(frame4, text="Export as .csv").grid(column=0, row=1)





root.mainloop()