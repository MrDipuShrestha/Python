# to generate random number we use random module
# to use random module first we have to inport it

import random

# generate ramdom integer number

random_integer = random.randint(1, 10)  #radint() function take two parameters, which is range , it between random number is generate
print(random_integer)                       # the parameter is included


# generate ramdom float number
# to generate higher float value we have to multiply
random_float = random.random()  * 5 #this generate ramdom float number between [0,1) 1 is excuded
print(random_float)  # 0.0 to 1.0