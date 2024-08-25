
# opening file on read mode

# with open("my_file.txt", mode="r") as file:
#     content = file.read()
#     print(content)

# opening file in write mode
# with open("my_file.txt", mode="w") as file:
#     file.write("Hello World!")

# opening file in appending mode

with open("my_file.txt", mode="a") as file:
    file.write("\nThis is the append mode.")
