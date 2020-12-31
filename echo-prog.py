# echo program that uses user input to writes to a file and saves it
# echo message > example.bat (creates example.bat containing "message")

import os
import sys

print('Welcome to the echo to file program')

print('Enter the command to begin string, EX: echo ')
cmd1 = input()

print('Enter the message to add to file')
message1 = input()

print('Name of text file?')
fileName = input()

# finalString = str(cmd1 + ' ' + message1 + ' ' + fileName)


echoMakeFile = str(cmd1) + (' ') + str('"') + str(message1) + ('"') + (' ') + str('>') + (' ') + str(fileName)

# print(echoMakeFile)

def echoFile():
    print('Now executing the echo program')
    res = os.system(echoMakeFile)


echoFile()
