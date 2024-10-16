
#use dbwrite when you need to write multiple things (may be helpful for GUI box cords??)

import sqlite3

database = 'projects.db'

def dbwrite(database):

    #SQL DB
    connection = sqlite3.connect(database)
    #cursor used to read/write into db
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO projects (name, date)
    VALUES (?,?)
    ''', ('newtest', 'newtest'))

    #Commit the transaction
    connection.commit()

    #Close the cursor and connection
    cursor.close()
    connection.close()
        
def main():
    dbwrite(database)
    print('done')

main()