
#functions to support app.py (RedEye Computer Vision Application)

#variables to feed?
#cap -> the video source
# Target width and height???
#video_frame -> is where the video will be placed in the app (is a tkinter label)



from tkinter import *
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

#Function to update video frame in tkinter app
def update_frame(cap, video_frame, TARGET_WIDTH, TARGET_HEIGHT):
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