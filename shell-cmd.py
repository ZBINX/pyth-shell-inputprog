# Program that will ask you for commands that will be executed in the shell

import os
import sys

def pwd():
    print('Execuating PWD command')
    global res
    res = os.system('pwd')
    shellResult()
    

def ls():
    print('Execuating LS command')
    global res
    res = os.system('ls')
    shellResult()

def lss():
    print('Execuating bad LSS command')
    global res
    res = os.system('lss')
    shellResult()
    

def lsblk():
    print('Execuating lsblk command')
    global res
    os.system('lsblk -a')
    shellResult()

def quit():
    print('Exiting program. Goodbye!')
    sys.exit()
    
def shellResult():
    if res == 0:
        print('shell command Success')
    else:
        print('shell command Failed')

while True:
    print('Enter a command:')
    command = input()

    if command == ('pwd'):
        pwd()
        
    elif command == ('ls'):
        ls()

    elif command == ('lsblk'):
        lsblk()

    elif command == ('lss'):
        lss()

    elif command == ('quit'):
        print('Program will exit now. Goodbye')
        quit()



        







