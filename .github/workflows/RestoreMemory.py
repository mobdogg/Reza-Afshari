import os
import socket
import sys
import datetime
import tarfile

class Timer(object):
    def __init__(self):
        pass
    def start(self):
        self.start = datetime.datetime.now()
        print ("0:00:00.000")
    def elapsed(self):
        print str(datetime.datetime.now() - self.start)[:-3]

watch=Timer()
watch.start()
tf = tarfile.open("checkpoint1.tgz")
tf.extractall()
sys.stdout.write("Checkpoint Extracted ")
watch.elapsed()
os.system("docker load -i looper.tgz")
os.system("docker create --name looper-clone busybox:latest /bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'")
os.system("docker start --checkpoint-dir=/migration/migration --checkpoint=checkpoint1 looper-clone")
sys.stdout.write("Checkpoint Restored")
watch.elapsed()

s = socket.socket()
s.connect(('192.168.0.104',8081))
data = "send"
s.send(data.encode());
s.close()
sys.stdout.write("Handover Completed ")
watch.elapsed()
