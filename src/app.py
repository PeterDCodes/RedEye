#main Flask app for RedEye


from flask import Flask, render_template

app = Flask(__name__)

#main start page of app (select or make new project)
@app.route("/")
def home_page():
    return render_template('index.html')


#page for creating new project
@app.route("/new")
def home_page():
    return render_template('new.html')


#app page for viewing project
@app.route("/project")
def home_page():
    return render_template('project.html')