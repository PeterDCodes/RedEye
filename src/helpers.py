#example
def my_function(arg):
    print(f"Button pressed: {arg}")
    # Additional logic based on `arg`

# function to update the model used in app
def change_model(model):
    model.set("Updated Value")
    print("Variable updated to:", model.get())


#function for opening files
# import filedialog module
from tkinter import filedialog
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files","*.txt*"), ("all files", "*.*")))

#function for viewing available camera ports
import cv2
def list_ports():
    """
    Test the ports and returns a tuple with the available ports and the ones that are working.
    """
    non_working_ports = []
    dev_port = 0
    working_ports = []
    available_ports = []
    while len(non_working_ports) < 6: # if there are more than 5 non working ports stop the testing. 
        camera = cv2.VideoCapture(dev_port)
        if not camera.isOpened():
            non_working_ports.append(dev_port)
        else:
            is_reading, img = camera.read()
            w = camera.get(3)
            h = camera.get(4)
            if is_reading:
                working_ports.append(dev_port)
            else:
                available_ports.append(dev_port)
        dev_port +=1
    return working_ports