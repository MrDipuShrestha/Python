alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(code_direction, text_message, shift_position):
        encrypt_message = ""
        if code_direction == "decode":
            shift_position *= -1
            
        for letter in text_message:
            position = alphabet.index(letter)
            next_position = position + shift_position
            new_message = alphabet[next_position]
            encrypt_message += new_message

        print(f"The encrypt message is {encrypt_message}")

ceaser(code_direction=direction, text_message=text, shift_position=shift)