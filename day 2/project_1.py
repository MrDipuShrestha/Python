
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height_in_float = float(height)
weight_in_float = float(weight)

bmi = int(weight_in_float / (height_in_float ** 2))

print(bmi)