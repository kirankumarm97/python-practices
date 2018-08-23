from socket import *
serverName='DESKTOP-4DQ5G1E'
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    
    file=open(sentence,"r")
    while file:
        l=file.read(1024)
        connectionSocket.send(l.encode())
    file.close()
    connectionSocket.close()
