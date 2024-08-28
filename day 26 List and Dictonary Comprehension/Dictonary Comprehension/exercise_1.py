sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_list = sentence.split()

sentence_dict = {letter: len(letter) for letter in sentence_list}

print(sentence_dict)
