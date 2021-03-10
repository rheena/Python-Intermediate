'''
Threading allows us to speed up our programs by executing multiple tasks at the same time with threads.
Threads are like lightweight processes coz they are a lot simillar to processes but need less resources.
Big advantage of using threads is they are in the same process in the same memory space and you can run multiple tasks at the same time.
'''

import threading

def helloworld(): #Creates the function of the thread class
    print('Hello World!')

#Creating a new object of the thread class and mention (not call) the fuction since you want to say that this is the function to be used.
t1 = threading.Thread(target=helloworld) 

#Use the start method to run the thread
t1.start()


#Executing two functions
def function1(): 
    for x in range(10000):
        print('ONE')

def function2(): 
    for x in range(10000):
        print('TWO')

t1 = threading.Thread(target=function1) 
t2 = threading.Thread(target=function2) 

t1.start()
t2.start()

#Waiting for threads 
def hello(): 
    for y in range(50):
        print('Hello!')

t1 = threading.Thread(target=hello) 
t1.start()

#This is to ensure that nothing else is executed until the main thread is done
t1.join() 

print('Another text')