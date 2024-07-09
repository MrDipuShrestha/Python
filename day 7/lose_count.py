import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ["college", "guitar", "piano"]
word = random.choice(words)
blank_list = ["_"] * len(word)
end_of_the_game = False
lives = 6

while not end_of_the_game: 
    letter = input("Guess the letter: ").lower()
    for n in range(len(word)):
        if letter == word[n]:
            blank_list[n] = letter
    print(blank_list)

    if letter not in word:
        lives -= 1
        if lives == 0:
            end_of_the_game = True
            print("You lose.")


    if "_" not in blank_list:
        end_of_the_game = True
        print("You won")
    print(stages[lives])

   
        

    
    