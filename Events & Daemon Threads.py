#Events are things in python that we can trigger and then react to them.
import threading
import time

event = threading.Event()

def myfunction():
    print('Waiting for event to trigger...\n')
    event.wait() #Makes the function to wait until the event is triggered
    print('Performing action xyz now...')

t1 = threading.Thread(target=myfunction)
t1.start()

x = input('Do you want the event to be triggered? (y/n) \n')
if x == 'Y':
    event.set()

#Daemon threads are running in the background and the script terminates eventhough they are still running since they are not vital to the program
path = 'text.txt'
text = ''

#For reading the text in the file
def readFile():
    global path, text
    while True:
        with open('text.txt', 'r') as f:
            text = f.read()
        time.sleep(3)

#For printing the text
def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()