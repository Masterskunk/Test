#! /usr/bin/env python3




number = input("enter a number\n")

while int(number) < 11:
    print(number)
    number = int(number) + 1
else:
    print("GameOver")
    number = number - 1
    
  


