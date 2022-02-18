#! /usr/bin/env python3

import os        
import subprocess

svc = input("enter a service to check and start:  ")

cmnd = ["ps", "-C", svc]

svc_check = subprocess.call(cmnd) ## This will run the cmnd as a subrpocess


if svc_check == 0: ## this will output same as from echo $?
    print ("Process running")
else:
    print ("Service not started")
    subprocess.call(["systemctl", "restart", svc])
    subprocess.call(cmnd)