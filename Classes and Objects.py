'''
Object oriented programming is a programming paradigm that tries to model the real world (books, computers, cars) into the programming world.
To do so, we use classes and objects. 
A CLASS is a blueprint of the object and the actual object to be an instance of this class.
We create objects of a class by calling a constructor. A constructor is a method in the class that we need to call whenever we call an object.
The def__init__(self)method calls the constructor or is the constructor and takes at leasr one parameter which is self.
The (self) parameter is a parameter that has to be in every method/function we define for the class coz it refers to the object we are using rn.
'''
#When declaring the same value all through
class Person:  

    def __init__(self):
        self.name = 'Rhee'
        self.age = 25

Person1 = Person()
print(Person1.name)
print(Person1.age)

#Accepting some parameters then assigning the values of this parameters to the attributes of the class of the object
class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
 
Person1 = Person('Rhee', 25, 155)
print(Person1.name)
print(Person1.age)
print(Person1.height)

Person2 = Person('Dee', 28, 152)
print(Person2.name)
print(Person2.age)
print(Person2.height)

#Changing the set values of the attribute
Person1.name = 'Jenny'
print(Person1.name)


#Other predefined methods
#Constructor
class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def helloWorld(self):
        print('Hello world!')

Person1 = Person('Rhee', 25, 155)
print(Person1.name)
print(Person1.age)
print(Person1.height)

Person1.name = 'Jenny'
print(Person1.name)
Person1.helloWorld()

#Destructor
class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __del__(self):
        print('object deleted!')

Person1 = Person('Rhee', 25, 155)
print(Person1.name)
print(Person1.age)
print(Person1.height)

Person1.name = 'Jenny'
print(Person1.name)

#del keyword deletes an object or value
del Person1


#STR function - helps determine what happend when I print my object or to define what happens when I convert into a string or typecast the values
class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return 'Name: {}, Age: {}, Height: {}'.format(self.name, self.age, self.height)

Person1 = Person('Rhee', 25, 155)
print(Person1.name)
print(Person1.age)
print(Person1.height)

print(Person1)

#Class variables - this are variables that are not unique for each object but are the same value for each object
class Person:

    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):
        Person.amount -= 1

    def __str__(self):
        return 'Name: {}, Age: {}, Height: {}'.format(self.name, self.age, self.height)

'''    def get_older(years):
        self.age += years'''

Person1 = Person('Rhee', 25, 155)
print(Person1)

Person2 = Person('Dee', 28, 152)

print(Person.amount)
