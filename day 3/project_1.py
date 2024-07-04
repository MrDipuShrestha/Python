print("Welcome to Pyhton Pizza Delivery.")

size = input("What size do you want? S, M, L.")



bill = 0

if size == "S":
    print("Price: $15")
    bill += 15
elif size =="M":
    print("Price: $20")
    bill += 20
else:
    print("Price: $25")
    bill += 25

add_pepperoni =  input("Do you want to add pepperoni? Y or N.")

if add_pepperoni == "Y":
    print("Price: $2")
    bill += 2

extra_cheese = input("Do you want extra cheese? Y or N.")
if extra_cheese == "Y":
    print("Price: $3")
    bill += 3

print(f"Your total bill is ${bill}")