#! /usr/bin/env python3

        
import os

file = input("Enter a file to create")

if os.path.isfile(file):
    print ("file does exist")
else:
    print ("the file does not exist, creating the file")
    os.system('touch {}.py'.format(file))
    os.system('chmod +x {}.py'.format(file))
    os.system('ls')
    
    