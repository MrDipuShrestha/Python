
age = input("Enter your age: ")

age_as_int = int(age)

year_remaining = 90 - age_as_int
months_remaining = 12 * year_remaining
weeks_remaining = 52 * year_remaining
days_remaining = 365 * year_remaining

print(f"You have {months_remaining} months, {weeks_remaining} weeks, {days_remaining} days remaining.")
