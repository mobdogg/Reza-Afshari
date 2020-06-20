#!/usr/bin/env python

import socket
import time
import os
import sys
import datetime

class Timer(object):
    """A simple timer class"""
    
    def __init__(self):
        pass
    
    def start(self):
        """Starts the timer"""
        self.start = datetime.datetime.now()
    
    def stop(self):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        print str(self.stop - self.start)
    def elapsed(self):
        """Time elapsed since start was called"""
        print str(datetime.datetime.now() - self.start)[:-3]
    
watch=Timer()

listensocket = socket.socket()
port=8080
ip = socket.gethostname()
listensocket.bind(('',port))
listensocket.listen(5)
print("Waiting for connection...")
clientsocket, client_address = listensocket.accept()
print("Connected")
sys.stdout.write("Starting ")
watch.start()
#os.system("docker run -d --name looper busybox:latest \
         #/bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'")
running=True
while running:
        message = clientsocket.recv(1024).decode()
    	if not message == "":
	    sys.stdout.write("Order received ")
	    watch.elapsed()
	    os.system("python hosta.py")
            time.sleep(0)
    	else:
            clientsocket.close()
            running = False
