print("Welcome to the Treaure Hunt")
print("Your mission is to find the treasure")
print("--------------------------------------")
print("You are currently in a dark room with only a torch to light your way")
print("You are walking in a straight path. After walking few moment, path get divide.")
print("-----||||----")
first = input("Which way do you want to go? Left or Right ")
first_lowercase = first.lower()

if first_lowercase == "left":
    print("You are in a room with a river middle on it.")

    print("You can either wait in the room or swim across it.")

    print("------------------")
    second = input("What you want to do? Wait or Swim. ")

    second_lowercase = second.lower()
    if second_lowercase == "wait":
        print("You are waiting in the room for a long time. After that, 3 doors appear.")

        print("------------")
        third = input("Which door you want to go? Red or Blue or Yellow. ")

        third_lowercase = third.lower()
        if third_lowercase == "red":
            print("You are in a room with a big snake.")
            print("You are dead. Game Over.")
        elif third_lowercase == "blue":
            print("You are in a room with a big spider.")
            print("You are dead. Game Over.")
        else:
            print("You are in a room of big treasure.")
            print("You won the game. Congratulations!!")  
    else:
        print("You are no match for the water.")
        print("You are dead. Game Over")
else:
    print("You fall in to the hole.")
    print("You are dead. Game Over")

