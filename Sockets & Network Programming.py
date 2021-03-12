#Sockets are just the end point of a communication channel.
import socket

#Create a socket and pass which kind of socket (internet socket) and the protocol (TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Create a server. Make sockets that listens for input and another socket (client) that connects to the first socket.
s.bind(('127.0.0.1', 55555)) #IP address and port
s.listen() #Puts socket to listening mode

while True:
    client, address = s.accept() #Accpets every single client
    print('Connected to {}'.format(address)) 
    client.send('You are connected!'.encode()) 
    client.close()


