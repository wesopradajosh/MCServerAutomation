# Audit Logger by Joshua Dimery
# Objective: This script should allow you to check your Minecraft server's logs and find specific events
#   Ex. Did an operator spawn in something they weren't supposed to?
# 

import re
import sys

pathToLog = "Path/To/Log"
keyword = input("Please type in keyword you are looking for...\nReminder: Cap sensitive\n")


file = open(pathToLog, "r")

with open(logFile, "a") as f:
    f.write(str(timeOfBackup) + "Manual Remote backup failed, file could not be found!")