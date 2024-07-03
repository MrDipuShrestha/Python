# data type conversion

num_char = len( input("What is your name?"))

#type() function check the data type of variable

print(type(num_char)) 

#convertig int to string
new_num_char = str(num_char)
print(type(new_num_char))

# string and integer cannot be concat so we have to cnvert int to string using str() function

print("Your name has " + new_num_char + " characters.")