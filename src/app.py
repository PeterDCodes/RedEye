from tkinter import *
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
from helpers import my_function, change_model


#initialize application
root = Tk()
root.title('RedEye')
root.geometry("1200x800")

#root.iconbitmap('path to .ico file') USE THIS TO SET AN APP ICON

#styles of the application (This is like a .CSS file)
style = ttk.Style()
style.theme_use('alt') #NEED TO FIX THIS BASED ON OS. MAC can use AQUA but windows can not!!!!!
#title text style
style.configure("Title.TLabel", font=('Arial Black', 24))
#small button style
style.configure("Small.TButton", foreground = "white", background="black", borderwidth=0)
#large button style
style.configure("Large.TButton", foreground = "Black", background="Red", borderwidth=2, font=('Arial Black', 12))
#heading style
style.configure("Heading.TLabel", font=('Arial Black', 12))

#initialize Applications Variables
# Initialize the model as a StringVar
model = StringVar(value='No Model')
print(model.get())



#create root frame widgets
frame1 = ttk.Frame(root, padding=10, border=5, relief="solid")
frame2 = ttk.Frame(root, padding=0, border=5, relief="solid")
frame3 = ttk.Frame(root, padding=10, border=5, relief="solid")
frame4 = ttk.Frame(root, padding=10, border=5, relief="solid")

# Place the frames in a 2x2 grid
frame1.grid(row=0, column=0, sticky="nsew")  # Top-left
frame2.grid(row=0, column=1, sticky="nsew")  # Top-right   #ns = north south. nsew means the frame will fill expand in all directions?
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

# Configure weight for frame1 sub-frames
frame1.grid_rowconfigure(0, weight=1) #says the first row of frame 1 will have weight 1
frame1.grid_rowconfigure(1, weight=4) #says the seconds row of frame 1 will have weight 4
frame1.grid_columnconfigure(0, weight=1) #says the column (only 1) in frame 1 will have weight 1

#place sub-frames within frame1
frame1A.grid(row=0, column=0, sticky="nsew")
frame1B.grid(row=1, column=0, sticky="nsew")

# Configure the grid for frame1A and frame1B
frame1A.grid_rowconfigure(0, weight=1)
frame1A.grid_columnconfigure(0, weight=1)
frame1B.grid_rowconfigure(0, weight=1)
frame1B.grid_columnconfigure(0, weight=1)


#text for camaera frame title in frame1 sub box
ttk.Label(frame1A, text="Camera Frame Title", anchor=CENTER, style="Title.TLabel").grid(column=0, row=0, sticky="nsew")



video_frame = ttk.Label(frame1B)
video_frame.grid(row=0, column=0)
video_frame.grid_rowconfigure(0, weight=1)
video_frame.grid_columnconfigure(0, weight=1)



# #----------------------VIDEO FEATURE IN FRAME 1
# # Open video source (default is the webcam)
cap = cv2.VideoCapture(0)

# # Get the original frame size
original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Calculate the aspect ratio
aspect_ratio = original_width / original_height

#Example: Shrink to a target width, calculate height to maintain aspect ratio
# Get the width of the window and the frame widget
window_width = root.winfo_width()
widget_width = frame1B.winfo_width()
#Should set target width to be the current width of the frame?????
TARGET_WIDTH = 250 * widget_width  
TARGET_HEIGHT = int(TARGET_WIDTH / aspect_ratio)

# #Function to update video frame in tkinter app
def update_frame():
        ret, frame = cap.read()  # Capture frame-by-frame
        if ret:
            # Get the current size of frame1B
            frame1B.update_idletasks()
            frame1b_height = frame1B.winfo_height()

            TARGET_HEIGHT = frame1b_height
            if(TARGET_HEIGHT > 200):
                 TARGET_HEIGHT = TARGET_HEIGHT - 150
            TARGET_WIDTH = int(TARGET_HEIGHT * aspect_ratio)


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
        video_frame.after(10, update_frame)  # Update every 10 ms

update_frame()


#frame2
#create sub-frames within frame2
frame2A = ttk.Frame(frame2, padding = 10, border=5, relief="solid")
frame2B = ttk.Frame(frame2, padding = 10, border=5, relief="solid")
frame2C = ttk.Frame(frame2, padding = 10, border = 5, relief="solid")

#frame2 grid configure for dynamic resizing
frame2.grid_rowconfigure(0, weight=1)
frame2.grid_rowconfigure(1, weight=1)
frame2.grid_rowconfigure(2, weight=1)
frame2.grid_columnconfigure(0, weight=1)



#place sub-frames within frame2
frame2A.grid(row=0, column=0, sticky="nsew")
frame2B.grid(row=1, column=0, sticky="nsew")
frame2C.grid(row=2, column=0, sticky="nsew")

#column titles
ttk.Label(frame2A, text="Set-Area").grid(column=0, row=0)
ttk.Label(frame2A, text="Area Name").grid(column=1, row=0)
ttk.Label(frame2A, text="Coordinates").grid(column=2, row=0)
ttk.Label(frame2B, text='Class Selection').grid(column=0, row=0, columnspan=2)
ttk.Label(frame2C, text="Object Editor", style='Heading.TLabel').grid(column=0, row=0)

#list of buttons, name entrys, and coordinate displays in frame 2. uses loop to add all the items
button_count = 10 #will use this based on number of areas of interest allowed. Max 10??
for i in range(button_count):
    ttk.Button(frame2A, text=f'Button{i + 1}', command=lambda arg=f'Button{i + 1}': my_function(arg), style="Small.TButton").grid(column=0,row=i+1, sticky="nsew") #row is i+1 because title is at position 0 
    ttk.Entry(frame2A).grid(column=1,row=i+1)
    ttk.Label(frame2A, text="coordinates need to go here").grid(column=2, row=i+1)



#function to update the checkboxes in frame 2B for class selection. NEED TO MIGRATE TO HELPERS FILE
def update_checkboxes():
    # Clear existing checkboxes below row 0
    for widget in frame2B.winfo_children():
        info = widget.grid_info()
        if info['row'] > 0:
            widget.destroy()
    
    #class selection box in frame 2
    #use a loop to add checkboxed based on list of objects
    # Check the value of the model and update checkboxes
    if model.get() == "Updated Value":
        objects = ['stap', 'PCBA', 'cell', 'pack', 'Fixture']  # Temporary list of classes
        for i, obj in enumerate(objects):
            ttk.Checkbutton(frame2B, text=obj).grid(column=0, row=i+1, sticky="nsew")

#model selection for frame 2
ttk.Button(frame2C, text="Select Vision Model", style="Large.TButton",
           command = lambda: (change_model(model), update_checkboxes(), print(model.get()))).grid(column=0, row=1, sticky="nsew") #frame 2B is updated since it contains the object classes derrived from a model
frame2C.grid_columnconfigure(0,weight=1)
frame2C.grid_rowconfigure(0,weight=1)
frame2C.grid_rowconfigure(1,weight=1)

#frame3
ttk.Label(frame3, text="Camera Manager", style="Heading.TLabel", anchor=CENTER).grid(column=0, row=0, sticky="nsew")
ttk.Button(frame3, text="Camera Config Button", style="Large.TButton").grid(column=0, row=1, sticky="nsew")
frame3.grid_columnconfigure(0,weight=1)
frame3.grid_rowconfigure(0,weight=1)
frame3.grid_rowconfigure(1,weight=1)



#frame4
ttk.Label(frame4, text="Start Data Export", anchor=CENTER, style="Heading.TLabel").grid(column=0, row=0, sticky="nsew")
ttk.Button(frame4, text="Export as .csv", style="Large.TButton").grid(column=0, row=1, sticky="nsew")
frame4.grid_columnconfigure(0,weight=1)
frame4.grid_rowconfigure(0,weight=1)
frame4.grid_rowconfigure(1,weight=1)

root.mainloop()

cap.release()