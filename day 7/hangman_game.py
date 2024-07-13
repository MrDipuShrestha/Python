import random

from hangman_words import words
word = random.choice(words)
blank_list = ["_"] * len(word)
end_of_the_game = False
lives = 6

from hangman_art import logo
print(logo)

print(blank_list )
while not end_of_the_game: 
    letter = input("Guess the letter: ").lower()
    print(f"You have already guesses {letter}")
    for n in range(len(word)):
        if letter == word[n]:
            blank_list[n] = letter
    print(blank_list)

    if letter not in word:
        lives -= 1
        print(f"You guesses {letter} which is not in word. You loose a life.")
        if lives == 0:
            end_of_the_game = True
            print("You lose.")
            print(f"The word is {word}")

    if "_" not in blank_list:
        end_of_the_game = True
        print("You won")
    
    from hangman_art import stages
    print(stages[lives])


   
        

    
    