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
os.system("docker load -i database.tgz")
os.system("docker create --name database -e mysql_root_password=123456 database")
os.system("./docker-volumes.sh database load database-volumes.tgz")
os.system("docker start database")
sys.stdout.write("Checkpoint Restored")
watch.elapsed()

s = socket.socket()
s.connect(('192.168.0.106',8081))
data = "send"
s.send(data.encode());
s.close()
sys.stdout.write("Handover Completed ")
watch.elapsed()
