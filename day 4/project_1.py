print("Treasure Map")

item1= ["◻️", "◻️", "◻️"]
item2= ["◻️", "◻️", "◻️"]
item3= ["◻️", "◻️", "◻️"]

map = [item1, item2, item3]

print(f"{item1}\n{item2}\n{item3}")

treasure_position = input("Where do you want to place treasure: ")

trasure = "X"

horizental = int(treasure_position[0])-1
vertical = int(treasure_position[1])-1

map[horizental][vertical] = trasure

print(f"{item1}\n{item2}\n{item3}")

