#! /usr/bin/env python3


 

def my_function(): 
	global mynum1
	mynum1 = 10 
	mynum2 = 20 
	print(mynum1 + mynum2) 


my_function()

print(mynum1)
