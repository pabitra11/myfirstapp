import socket

ssocket = socket.socket()

print('socket created')

ssocket.bind(('localhost', 9999))

ssocket.listen(5)

print('waiting for connection')

while True:
    Csocket, adds = ssocket.accept()
    name = Csocket.recv(1024).decode()
    print('connected with', adds, name)
    Csocket.send(bytes('welcome to my chat room','utf-8'))

    Csocket.close()
