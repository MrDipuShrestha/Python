# take a input of a and b and while printing switch value of each other  i.e a=b and b=a

a = input("a: ")
b = input("b: ")

temp = a
a = b
b = temp

print("a:" + a)
print("b:" +b)