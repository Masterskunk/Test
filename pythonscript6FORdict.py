#! /usr/bin/env python3

a_dict = {'color':'blue' , 'pet':'dog' , 'furniture':'chair'}

for key in a_dict: 
    print(key, '-->', a_dict[key])

###This is how the item relates to key
d_items = a_dict.items()
print(d_items)

for key, value in a_dict.items():
    print (key, '-->', value)

#######
print("WHO LET THE DOGS OUT \n")
    
for key , value in a_dict.items():
    if value == 'dog':
        print(value , " ", "Im a big dog")
    elif value == 'chair':
        print(value , " ", "Im a furniture not a dog")
    else:
        print(value , " ", "Im a fruit or something else")
        print(len(a_dict))
            
    
    