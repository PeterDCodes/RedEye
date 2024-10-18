import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading

def update_frame():
    while True:
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            break

        # Convert the frame to a format Tkinter can display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)

        # Update the image in the label
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

        # Refresh the GUI
        root.update_idletasks()
        root.update()

# Initialize the main window
root = tk.Tk()
root.title("Video Stream")
root.geometry("500x500")

# Create a label to display the video
video_label = ttk.Label(root)
video_label.pack()

# Open video source (default is the webcam)
cap = cv2.VideoCapture(0)

# Start the video update thread
video_thread = threading.Thread(target=update_frame)
video_thread.daemon = True
video_thread.start()

# Start the GUI event loop
root.mainloop()

# Release the webcam when done
cap.release()
cv2.destroyAllWindows()