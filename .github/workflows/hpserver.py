#!/usr/bin/env python

import socket
import time
import os
from binascii import unhexlify



listensocket = socket.socket()
port=8080
ip = socket.gethostname()
listensocket.bind(('',port))
listensocket.listen(5)
clientsocket, client_address = listensocket.accept()
os.system("docker run -d --name looper busybox:latest \
         /bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'")
running=True
while running:
        message = clientsocket.recv(1024).decode()
    	if not message == "":
	    print("Waiting for Handover Complete")
	    fullData = "Connected"
	    clientsocket.send(fullData.encode())
	    os.system("python hosta.py")
            time.sleep(0)
    	else:
            clientsocket.close()
            running = False
