#main Flask app for RedEye
#--------Test DB script-------
# import sqlite3

# #SQL DB
# connection = sqlite3.connect('projects.db')
# #cursor used to read/write into db
# cursor = connection.cursor()

# cursor.execute('''
# INSERT INTO projects (name, date)
# VALUES (?,?)
# ''', ('test', 'test'))

# #Commit the transaction
# connection.commit()

# #Close the cursor and connection
# cursor.close()
# connection.close()


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')