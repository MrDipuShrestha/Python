import random

print("Guess the word.")

words = ["college", "guitar", "piano"]

word = random.choice(words)

letter = input("Guess the letter:").lower()

for n in range(len(word)):
    if letter == word[n]:
        print("right")
    else:
        print("wrong")



    