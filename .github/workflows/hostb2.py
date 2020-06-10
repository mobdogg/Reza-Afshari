import os
import socket
import sys
from datetime import datetime 

os.system("docker create --name looper-clone oraclelinux:8.2 \ /bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'")
os.system("docker start --checkpoint-dir=/migration/migration --checkpoint=checkpoint1 looper-clone")
sys.stdout.write("Checkpoint Restored ")
print datetime.now().strftime('%H:%M:%S.%f')[:-4]

s = socket.socket()
s.connect(('10.2.76.100',8081))
str = "send"
s.send(str.encode());
s.close()
sys.stdout.write("Handover Completed ")
print datetime.now().strftime('%H:%M:%S.%f')[:-4]
exit()
