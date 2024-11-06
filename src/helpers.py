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
    print('hi')