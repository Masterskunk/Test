#! /usr/bin/env python3




number = ("one" , "two", "Three")

for item in number:
    print(item)

phrase = ("this is a sentence")

for item in phrase:
    print("\n" + item)

import random
counter = random.randint(1, 12)

number = 1

for i in range(counter):
    print(number)
    number +=3
    
    