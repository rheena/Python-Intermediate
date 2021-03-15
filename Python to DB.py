#Loading an object frpm a python script as a python object into the databse
import sqlite3

class Person:

    def __init__(self, id_number=-1, first='', last='', age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()

    def load_person(self, id_number):
        self.cursor.execute('''
        SELECT * FROM Persons
        WHERE id = {}
        '''.format(id_number))

        results = self.cursor.fetchone()

        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

    def insert_person(self):
        self.cursor.execute('''
        INSERT INTO Persons VALUES
        ({}, '{}', '{}', {})
        '''.format(self.id_number, self.first, self.last, self.age))

        self.connection.commit()
        self.connection.close()

p1 = Person(4, 'Alfred', 'Mambo', 28)
p1.insert_person()

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM Persons')
results = cursor.fetchall()
print(results)

connection.close()

