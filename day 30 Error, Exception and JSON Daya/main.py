# Exception handler

try:
    file = open("data.txt")
    data_dict = {"key": "value"}
    print(data_dict["key"])

except FileNotFoundError:
    file = open("data.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} doesn't exist")

else:
    file = open("data.txt")
    file = open("data.txt")
    print(file.read())

finally:
    file.close()
    print("The file is closed.")

    raise TypeError("This is the error i made.")


# height = float(input("Enter Height:"))
# weight = int(input("Enter Weight:"))

# if height > 3:
#     raise ValueError("Human height should not be over 3.")

# bmi = weight / height**2

print(bmi)
