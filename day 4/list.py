
new_list = ["dipesh","sayara","anil","sonam","sunita"]

print(new_list[0]) #positive index indiacte from front
print(new_list[3])
print(new_list[-2]) # neagtive index point from rear
print(new_list[-1])

new_list.append("ashim") # this method add item to the rear of the list

new_list.extend(["sapana","nijal"]) # this methos append list to the rear of the list

print(new_list)

# mergint two or more list

fruit = ["apple", "banana", "mango"]
vegies = ["potato", "onion"]

all_together = [fruit, vegies]