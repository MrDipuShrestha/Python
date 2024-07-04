print("Welsome to love calculator")

name1 = input("What is your name? ")
name2 = input("What is his/her name? ")

concat_name = name1 + name2
lower_case_name = concat_name.lower()

t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")
true = t + r + u + e

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")
love = l + o + v + e

score = str(true) + str(love) 

print(f"Your score is {score}")
