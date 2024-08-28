import pandas

letter_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

letter_dict = {row.letter: row.code for (index, row) in letter_dataframe.iterrows()}

user_letter = input("Enter a word: ").upper()

phonetic_list = [letter_dict[letter] for letter in user_letter]

print(phonetic_list)
