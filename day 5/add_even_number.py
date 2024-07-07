print("Let's add even numbers only")

sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum += number
print(f"The sum of even number is {sum}")