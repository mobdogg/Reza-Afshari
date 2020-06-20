# -*- coding: utf-8 -*-

import paramiko
import tarfile
import os
import sys
import datetime
#from datetime import datetime


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
os.system("docker checkpoint create --checkpoint-dir=/migration looper checkpoint1")
sys.stdout.write("Checkpoint Created ")
watch.elapsed()

def tardir(path, tar_name):
    with tarfile.open(tar_name, "w:gz") as tar_handle:
        for root, dirs, files in os.walk(path):
            for file in files:
                tar_handle.add(os.path.join(root, file))
tardir('/migration', 'checkpoint1.tgz')
sys.stdout.write("Checkpoint Archived ")
watch.elapsed()

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.43.184",username="toshiba",password="123456")
#Raises BadHostKeyException,AuthenticationException,SSHException,socket error
sftp=ssh.open_sftp()
sftp.put('/migration/checkpoint1.tgz','/migration/checkpoint1.tgz')
sys.stdout.write("Handover Completed ")
watch.elapsed()

