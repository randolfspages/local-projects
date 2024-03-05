# import the sql library (sqlite)
# and  1. create a connection with the Database
# 2. create an Object for Cursor
# 3. and lastly close all connection at the end of the program


import sqlite3

# connection to the database (the name of the database)
connection = sqlite3.connect('mydatabase.db')
conObject = connection.cursor()  # object for the cursor


# CREATE
# next we create our tables example: employees table or professionals table
# conObject.execute(
#     'CREATE TABLE IF NOT EXISTS professionals(id INTEGER PRIMARY KEY, fname TEXT, lname TEXT, email TEXT, phone INTEGER, location TEXT, jobTitle TEXT, field TEXT')
# connection.commit()


# 1. INSERT
def insert_data(id, fname, lname, email, phone, counrty, jobTitle, field):
    conObject.execute('INSERT INTO professionals VALUES(?, ?, ?, ?, ?, ?, ?, ?)',
                    (id, fname, lname, email, phone, counrty, jobTitle, field))   
    connection.commit()
    
# 2. UPDATE
def update_jobTitle(fname, id):
    conObject.execute('UPDATE professionals SET fname = ? WHERE id = ?', (fname, id))
    connection.commit()
    
def update_jobTitle(lname, id):
    conObject.execute('UPDATE professionals SET lname = ? WHERE id = ?', (lname, id))
    connection.commit()
    
def update_jobTitle(email, id):
    conObject.execute('UPDATE professionals SET email = ? WHERE id = ?', (email, id))
    connection.commit()
    
def update_jobTitle(phone, id):
    conObject.execute('UPDATE professionals SET phone = ? WHERE id = ?', (phone, id))
    connection.commit()

def update_jobTitle(country, id):
    conObject.execute('UPDATE professionals SET country = ? WHERE id = ?', (country, id))
    connection.commit()
    
def update_jobTitle(jobTitle, id):
    conObject.execute('UPDATE professionals SET jobTitle = ? WHERE id = ?', (jobTitle, id))
    connection.commit()
    
def update_jobTitle(field, id):
    conObject.execute('UPDATE professionals SET field = ? WHERE id = ?', (field, id))
    connection.commit()

# 3. DELETE
def delete_data(id):
    conObject.execute('DELETE FROM professionals WHERE id = ?', (id,))
    connection.commit()
    
def delete_all():
    conObject.execute('DELETE FROM professionals')
    connection.commit()


# 4. FETCH DATA
def fetch_data():
    conObject.execute('SELECT * FROM professionals')
    result = conObject.fetchall()

    for data in result:
        print(data)
    
insert_data(6, 'Erica', 'Ama Asantewaa', 'ea@gmail.com', 18648484938, 'Damstadt', 'Data Engineer', 'IT')


fetch_data()

conObject.close()
connection.close()
