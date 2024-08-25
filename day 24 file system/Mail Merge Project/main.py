PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt", "r") as names:
    names = names.readlines()

with open("Input/Letters/starting_letter.txt", "r") as letter:
    letter_content = letter.read()
    for name in names:
        stripted_name = name.strip("\n")
        new_letter = letter_content.replace(PLACEHOLDER, stripted_name)
        with open(f"Output/ReadyToSend/letter_to_{stripted_name}.txt", "w") as complete_letter:
            complete_letter.write(new_letter)