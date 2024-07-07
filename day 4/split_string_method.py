# who will pay the bill today

import random

# input name and split those with character ',' and make it a list
name_string = input("Write the names spliting with comma: ") 
names = name_string.split(", ")

 # generate random number
length_list = len(names)
random_num = random.randint(0, length_list-1)

who_will_pay = names[random_num]

print( who_will_pay + " will gonna pay the bill.")
