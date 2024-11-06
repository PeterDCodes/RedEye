#example
def my_function(arg):
    print(f"Button pressed: {arg}")
    # Additional logic based on `arg`

# function to update the model used in app
def change_model(model):
    model.set("Updated Value")
    print("Variable updated to:", model.get())


