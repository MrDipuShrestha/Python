alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    def encrypt(text_message,shift_position):
        encrypt_message = ""
        for letter in text_message:
            position = alphabet.index(letter)
            next_position = position + shift_position
            new_message = alphabet[next_position]
            encrypt_message += new_message

        print(f"The encrypt message is {encrypt_message}")
    encrypt(text_message=text, shift_position=shift)  
else:
    def decrypt(text_message, shift_position):
        encrypt_message = ""
        for letter in text_message:
            position = alphabet.index(letter)     
            new_position = position - shift_position
            new_message = alphabet[new_position]
            encrypt_message += new_message

        print(f"The decrypt message is {encrypt_message}")
    decrypt(text_message=text, shift_position=shift) 

