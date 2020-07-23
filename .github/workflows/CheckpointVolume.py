# -*- coding: utf-8 -*-

import paramiko
import tarfile
import os
import sys
import ftplib
import datetime
import socket

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
    def now(self):
	print str(datetime.datetime.now())[:-3]

watch=Timer()
watch.start()
os.system("./docker-volumes.sh database save database-volumes.tgz")
os.system("docker save -o database.tgz database")
sys.stdout.write("Checkpoint Archived ")
watch.elapsed()

session = ftplib.FTP('192.168.0.110','toshiba','123456')
file = open('/snapshot/database-volumes.tgz','rb')                  
session.storbinary('STOR /snapshot/database-volumes.tgz', file)     
file = open('/snapshot/database.tgz','rb')                  
session.storbinary('STOR /snapshot/database.tgz', file)     
file.close()                                    # close file and FTP
session.quit()

port = 8282
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.110',port))
sys.stdout.write("Handover Completed ")
watch.elapsed()
s.close()
