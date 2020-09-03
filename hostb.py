import time 
import os
import sys
import socket
  
listensocket = socket.socket()
port=8282
ip = socket.gethostname()
listensocket.bind(('',port))
listensocket.listen(5)
clientsocket, client_address = listensocket.accept()
os.system("python hostb2.py")
exit()

