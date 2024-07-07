import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy way i.e password in order
password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)

number = ""
for num in range(0, nr_numbers):
    number += random.choice(numbers)

symbol = ""
for sym in range(0, nr_symbols):
    symbol += random.choice(symbols)

final_password = password + number + symbol
print(f"Your order password is {final_password}")

#hard way ie your password in mixed

password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for num in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for sym in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

final_password = ""
for pas in password_list:
    final_password += random.choice(password_list)

print(f"Your password is {final_password}")
