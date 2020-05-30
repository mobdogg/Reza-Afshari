import os
import socket


os.system("docker create --name looper-clone busybox:latest \ /bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'")
os.system("docker start --checkpoint-dir=/migration/migration --checkpoint=checkpoint1 looper-clone")

s = socket.socket()
s.connect(('10.12.110.197',8081))
str = "send"
s.send(str.encode());
s.close()
print("Completed Exit")
exit()
