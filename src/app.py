from tkinter import *
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

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
#create sub-frames within frame1
frame1A = ttk.Frame(frame1, padding = 10, border=5, relief="solid")
frame1B = ttk.Frame(frame1, padding = 10, border=5, relief="solid")

#place sub-frames within frame2
frame1A.grid(row=0, column=0, sticky="nsew")
frame1B.grid(row=1, column=0, sticky="nsew")



#text in frame1 sub boxes
ttk.Label(frame1A, text="Camera Frame Title").grid(column=0, row=0)
video_frame = ttk.Label(frame1B)
video_frame.grid(row=0, column=0)


#----------------------VIDEO FEATURE IN FRAME 1
# Open video source (default is the webcam)
cap = cv2.VideoCapture(0)

# Get the original frame size
original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Calculate the aspect ratio
aspect_ratio = original_width / original_height

# Example: Shrink to a target width, calculate height to maintain aspect ratio
TARGET_WIDTH = 900
TARGET_HEIGHT = int(TARGET_WIDTH / aspect_ratio)

#Function to update video frame in tkinter app
def update_frame():
        ret, frame = cap.read()  # Capture frame-by-frame
        if ret:
            #resize the frame
            frame_resized=cv2.resize(frame, (TARGET_WIDTH, TARGET_HEIGHT))
            # Convert the frame to a format Tkinter can display
            frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)

            # Update the image in the label
            video_frame.imgtk = imgtk
            video_frame.configure(image=imgtk)

            # Update the image in the label
            video_frame.imgtk = imgtk  # Keep a reference to avoid garbage collection
            video_frame.config(image=imgtk)

        # Schedule the next update
        video_frame.after(15, update_frame)  # Update every 15 ms

update_frame()


#frame2
#create sub-frames within frame2
frame2A = ttk.Frame(frame2, padding = 10, border=5, relief="solid")
frame2B = ttk.Frame(frame2, padding = 10, border=5, relief="solid")
frame2C = ttk.Frame(frame2, padding = 10, border = 5, relief="solid")

#place sub-frames within frame2
frame2A.grid(row=0, column=0, sticky="nsew")
frame2B.grid(row=1, column=0, sticky="nsew")
frame2C.grid(row=3, column=0, sticky="nsew")

#column titles
ttk.Label(frame2A, text="Activate").grid(column=0, row=0)
ttk.Label(frame2A, text="Area Name").grid(column=1, row=0)
ttk.Label(frame2C, text="Object Editor").grid(column=0, row=2)

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

cap.release()