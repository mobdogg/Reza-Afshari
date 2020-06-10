# -*- coding: utf-8 -*-

import paramiko
import tarfile
import os
import sys
from datetime import datetime

os.system("docker checkpoint create --checkpoint-dir=/migration looper checkpoint1")
sys.stdout.write("Checkpoint Created ")
print datetime.now().strftime('%H:%M:%S.%f')[:-4]
def tardir(path, tar_name):
    with tarfile.open(tar_name, "w:gz") as tar_handle:
        for root, dirs, files in os.walk(path):
            for file in files:
                tar_handle.add(os.path.join(root, file))
tardir('/migration', 'checkpoint1.tgz')
sys.stdout.write("Checkpoint Archived ")
print datetime.now().strftime('%H:%M:%S.%f')[:-4]

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.43.184",username="toshiba",password="123456")
#Raises BadHostKeyException,AuthenticationException,SSHException,socket error
sftp=ssh.open_sftp()
sftp.put('/migration/checkpoint1.tgz','/migration/checkpoint1.tgz')
