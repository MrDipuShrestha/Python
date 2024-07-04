

print("Welcome to Cable Car ride.")

age = int( input("What is your age? "))
bill = 0

if age < 5:
    print("You can ride for free.")
elif age >= 5 and age < 18:
    bill = 500
    print("You have to pay Rs500.")
else:
    bill = 1000
    print("You have to pay Rs1000.")

photo = input("Do you want to take photo? Y or N.")
if photo == "Y":    #this statement is execute always 
    print("You have to pay Rs200 for photo.")
    bill += 200

print(f"Your total bill is Rs.{bill}")


