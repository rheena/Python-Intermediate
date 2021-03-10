#locking helps to ensure that only 1 thread at a time can access the resource
import threading
import time

x = 8192

lock = threading.Lock()

#Keyword global states that I have a variable in my scrip that is not part of this function but I want to access and change it.
def double():
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1) #Sleep method tells the program to wait for a specified amount of seconds 
    print('Reached the maximum!')
    lock.release()

def half():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print('Reached the minimum!')
    lock.release()

t1 = threading.Thread(target=half)
t2 = threading.Thread(target=double)

t1.start()
t2.start()


