import random

print("Replace the guess the word.")

words = ["college", "guitar", "piano"]

word = random.choice(words)

letter = input("Guess the letter: ").lower()

blank_list = ["_"] * len(word)

for n in range(len(word)):
    if letter == word[n]:
        blank_list[n] = letter

print(blank_list)



    