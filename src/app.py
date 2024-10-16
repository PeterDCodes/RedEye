#main Flask app for RedEye


from flask import Flask, render_template

app = Flask(__name__)

#main start page of app (select or make new project)
@app.route("/")
def home_page():
    return render_template('index.html')

    # user will be able to select a project from dropdown box
    # or user can create new project


#page for creating new project
@app.route("/new")
def home_page():
    return render_template('new.html')

    #user will need to enter all project information
    #user can exit and return home



#app page for viewing project  MOST CODE WILL NEED TO BE HERE
@app.route("/project")
def home_page():
    return render_template('project.html')

    #user can exit the project and return home
    #placeholder for camera feed will be in the middle left of screen
    #right side of screen will contain 3 areas
        #camera set up
        #station config
        #data export config
    