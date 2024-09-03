fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit)
    except IndexError as error_message:
        print(f"{error_message}")

    else:
        print(fruit + "pie")


make_pie(4)
