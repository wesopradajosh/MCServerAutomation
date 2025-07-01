import paramiko
import sched
import os
import shutil
import datetime
import pathlib
import logging

import paramiko.sftp
import paramiko.sftp_client

# This code does not use a scheduler and is a manual backup script
# This script uses RSA keys to access the device as its more secure

dstIP = "192.168.1.0"
remoteUser = "user"
pathToFile = 'Path/To/The/File/You/Want/To/Copy'
pathToSave = 'Path/To/The/Location/You/Want/To/Save/To'
keyPath = 'Path/To/Your/Public/Key'
logFile = 'Path/To/Your/Log/File'
nameOfFile = os.path.basename(pathToFile)
timeOfBackup = datetime.datetime.now()
timestamp = timeOfBackup.strftime("%Y%m%d_%H%M%S")
mykey = paramiko.RSAKey.from_private_key_file(keyPath)




try:
     if os.path.exists(pathToFile):
          print("File is found!")

          print("Setting up SSH connection")
          ssh = paramiko.SSHClient()
          ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


          
          ssh.connect(hostname=dstIP, username=remoteUser, pkey=mykey)
          print("SSH Connection successful!")
          remoteFilePath = F"{pathToSave}/{str(timestamp)}_{nameOfFile}"

          sftpSes = ssh.open_sftp()

          sftpSes.put(pathToFile, remoteFilePath)

          print("Performing backup...")
          sftpSes.close()
          



          print("Backup performed at: " + str(timeOfBackup))
          with open(logFile, "a") as f:
            f.write(str(timeOfBackup) + "Successful manual remote backup!")


     else:
          print("error while locating file!")
          with open(logFile, "a") as f:
               f.write(str(timeOfBackup) + "Manual Remote backup failed, file could not be found!")

except Exception as e:
      print("FATAL ERROR", e)
      with open(logFile, "a") as f:
        f.write(str(timeOfBackup) + "Manual Remote backup failed, Reason: " + str(e) + "\n")
      
     




