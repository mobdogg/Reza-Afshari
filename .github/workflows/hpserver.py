#!/usr/bin/env python
from cryptography.fernet import Fernet
import socket
import time
import os

listensocket = socket.socket()
port=8080
ip = socket.gethostname()
listensocket.bind(('',port))
listensocket.listen(5)
clientsocket, client_address = listensocket.accept()
print("Connected")
running=True
while running:
        message = clientsocket.recv(1024).decode()
    	if not message == "":
	    print("Waiting for Handover Complete")
            os.system("python hosta.py")
            time.sleep(0)
    	else:
            clientsocket.close()
            running = False
