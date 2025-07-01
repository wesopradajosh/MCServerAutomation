# Telraw Generator by Josh
# Grab random sentences in a file and send them to the Minecraft server via MCRon as telraw msgs.


from mcrcon import MCRcon
import random

host = "192.168.1.0"
password = "Password"
port = 25575 # default port

filePath = "Path/to/message.txt"

messageArr = []

 

with open(filePath, 'r') as f:
    for line in f:       
        messageArr.append(line.strip())

chosenMsg = random.randint(0,len(messageArr) - 1)
print("Selected message = " + messageArr[chosenMsg])

# This was for testing if the messages got saved to the array, spoiler alert it worked

#for i in range (len(messageArr)):

#   print(messageArr[i])



with MCRcon(host, password, port) as mcr:
    response = mcr.command(f'tellraw @a {messageArr[chosenMsg]}')
    print(response)






      
 





