# MCServerAutomation
Automation scripts for a Minecraft server using python run on an Ubuntu Server

## ManBackup.py:
-  The script can just be ran automatically via crontab on linux or via task scheduler on windows
-  Script that automates server backups through manual use and saves to a remote server. Provides redundancy for my server in the event something happens to it on a hardware level.
-  Makes use of public/private RSA keys for better security.

  To Do:
  
  -  WAIT IM STUPID I COULD JUST ZIP THE FOLDER INSTEAD OF USING THAT RECURSIVE LOOP TO SEND ALL THE DATA, IDK HOW I DIDNT THINK OF THAT LOL

## AuditLogger.py
This script is used to easily scan audit logs for specifc keywords

  To Do:
  
  -  I might make it so it grabs a list of keywords that it scans for in the logs every few minutes (ex. someone spawning in something) I would probably have to implement some notification system via Discord.

## TellrawGen.py
This script grabs sentences from a txt file and uses mcrcon to access the server to automatically send tellraw messages every few minutes using crontab.

  To Do:
  
  -  Ill think of something
