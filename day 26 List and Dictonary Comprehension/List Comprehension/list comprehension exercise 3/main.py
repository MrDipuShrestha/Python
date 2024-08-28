
with open("file1.txt") as first_file:
    # first_list = [int(number.strip()) for number in first_file]
    first_list = first_file.readlines()
with open("file2.txt") as second_file:
    # second_list = [int(number.strip()) for number in second_file]
    second_list = second_file.readlines()

# common_numbers = [number for number in first_list if number in second_list]
common_numbers = [int(number) for number in first_list if number in second_list]

print(common_numbers)
