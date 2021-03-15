#Basic database used is called SQLite 3
import sqlite3

class Person:

    def __init__(self, id_number, first, last, age):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age

        #Creating a connection to a database
        self.connection = sqlite3.connect('mydata.db')

        #Cursor is the object or interface to the db. This allows us to execute database queries. 
        self.cursor = connection.cursor()


#Creating a method that loads a person from the table and converts it into a python object
    def load_person(self, id_number):
        cursor.execute('''
        SELECT * FROM Persons
        WHERE id = {}
        ''').format(id_number)

        results = cursor.fetchone()

        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

#Creating a new table in the database
cursor.execute('''
CREATE TABLE IF NOT EXISTS Persons (
    id INTEGER PRIMARY_KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
''')

cursor.execute('''
INSERT INTO Persons VALUES
(1, 'Darleen', 'Macharia', 28),
(2, 'Maureen', 'Macharia', 32),
(3, 'Annie', 'Kobia', 23)
''')

cursor.execute('''
SELECT * FROM Persons
WHERE last_name = 'Macharia'
''')

rows = cursor.fetchall()
print(rows)

connection.commit()

connection.close()

