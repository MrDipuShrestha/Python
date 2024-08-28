# list comprehension
from re import split

# for List
# new_list = [new_item for item in list]

number = [1, 2, 3]
new_list = [n + 1 for n in number]

print(new_list)


# for string

# new_list = [ letter for letter in name]

name = "Dipesh"
new_list = [letter for letter in name]

print(new_list)

# using range

range_list = [number * 2 for number in range(1, 5)]
print(range_list)

# Conditional List Comprehension

# new_list = [new_item for item in list if test]

names = ['Dipesh', 'Sayara', 'Riya', 'Ashim', 'Nijal']

capital_names = [name.upper() for name in names if len(name) > 4]

print(capital_names)