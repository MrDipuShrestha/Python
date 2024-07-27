# Python doesn't contain block scope

game_level = 3

enemies = ["skleton", "zombie"]

if game_level < 5:
    new_enemy = enemies[
        0
    ]  # this variabel is in block scope i.e it's in a if.. block. although it can be accessible from outside the block

print(new_enemy)
