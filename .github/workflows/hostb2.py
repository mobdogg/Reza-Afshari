import os
import socket
import sys
import datetime
import tarfile

class Timer(object):
    """A simple timer class"""
    
    def __init__(self):
        pass
    
    def start(self):
        """Starts the timer"""
        self.start = datetime.datetime.now()
        print ("0:00:00.000")
    
    def stop(self):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        print str(self.stop - self.start)
    def elapsed(self):
        """Time elapsed since start was called"""
        print str(datetime.datetime.now() - self.start)[:-3]
watch=Timer()
watch.start()
tf = tarfile.open("checkpoint1.tgz")
tf.extractall()
sys.stdout.write("Checkpoint Extracted ")
watch.elapsed()
#os.system("docker create --name looper-clone oraclelinux:8.2 \ /bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'")
#sys.stdout.write("Container Created ")
#watch.elapsed()
os.system("docker start -p 192.168.43.184:80:80 -w=/app --checkpoint-dir=/migration/migration --checkpoint=checkpoint1 looper-clone")
sys.stdout.write("Checkpoint Restored ")
watch.elapsed()

s = socket.socket()
s.connect(('10.33.211.110',8081))
data = "send"
s.send(data.encode());
s.close()
sys.stdout.write("Handover Completed ")
watch.elapsed()
exit()
