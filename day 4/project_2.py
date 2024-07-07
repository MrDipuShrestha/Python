import random

print("Rock Paper Scissor Game")

list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter 0 for Rock, 1 for paper and 2 for Scissor: ")
user_input = int(user_choice)
print(user_input)

list1 = ["Rock", "Paper", "Scissor"]
computer_choice = random.randint(0,2)
print(computer_choice)

print(f"Your choice: {list[user_input]}")
print(f"Computer's choice: {list1[computer_choice]}")

if user_input == 0 and computer_choice == 1 or user_input == 1 and computer_choice == 2 or user_input == 2 and computer_choice == 0:
    print("You lose")
elif user_input == 1 and computer_choice == 0 or user_input == 2 and computer_choice == 1 or user_input == 0 and computer_choice == 2:
    print("You win")
else:
    print("It's a tie")


