print("Welcome to Tip Calculator.")

total = input("What was the total bill? Rs.")
total_as_float = float(total)
tip = input("What percentage tip would you like to give? 10, 12, or 15? ") 
tip_as_int = int(tip)
people = input("How many people to split the bill? ")
people_as_int = int(people)

tip_in_rs= total_as_float * (tip_as_int/100)
total_with_tip = round(total_as_float + tip_in_rs, 2)

print(f"Each person should pay: {total_with_tip/people_as_int}")
