import socket

csocket = socket.socket()

csocket.connect(('localhost', 9999))
name = input('what is your name?')
csocket.send(bytes(name,'utf-8'))
print(csocket.recv(1024).decode())