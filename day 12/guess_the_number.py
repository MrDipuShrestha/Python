import random

print("Welcome to the number gussing game!")


def generate_number():
    """Generate the random number"""
    random_number = random.randint(1, 100)
    return random_number


def attempt(level):

    if level == "easy":
        return 10
    else:
        return 5


def check_number(user, random, attempt):
    if user == random:
        print(f"You got it. The answer was {random}.")
        return
    elif user > random:
        print("Too high.\nGuess again.")
        return attempt - 1
    else:
        print("Too low.\nGuess again.")
        return attempt - 1


def play_game():
    no_of_attempt = attempt(difficulty)

    rand_number = generate_number()

    user_number = 0
    while user_number != rand_number:
        print(f"You have {no_of_attempt} attempts to guess the number")
        user_number = int(input("Guess the number: "))
        no_of_attempt = check_number(user_number, rand_number, no_of_attempt)

        if no_of_attempt == 0:
            print("You are out of guesses. Try again.")
            return


print("I'm thining of a number between 1 and 100.")
difficulty = input("Choose a dificulty. Type 'easy' or 'hard': ")
play_game()
