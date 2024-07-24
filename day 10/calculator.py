# Calculator

# from art import logo


# Add
def Add(n1, n2):
    return n1 + n2


# Subtract
def Sub(n1, n2):
    return n1 - n2


# Multiplication
def Mult(n1, n2):
    return n1 * n2


# Division
def Div(n1, n2):
    return n1 / n2


def calculator():
    # print(logo)

    firstNumber = float(input("Enter the first number: "))
    operator = {
        "+": Add,
        "-": Sub,
        "*": Mult,
        "/": Div,
    }
    for symbol in operator:
        print(symbol)
    should_continue = True

    while should_continue:
        calculate_operator = input("Chose an operator : ")

        secondNumber = float(input("Enter the next number: "))

        calculate_function = operator[calculate_operator]

        result = calculate_function(firstNumber, secondNumber)

        print(f"{firstNumber} {calculate_operator} {secondNumber} = {result}")

        choice = input(
            "Type 'y' to continue calculating with {first_result}, or type 'n' to start new operation , or exit..: "
        )

        if choice == "y":
            firstNumber = result
        elif choice == "n":
            should_continue = False
            calculator()
        else:
            should_continue = False
            print("Thank You!")


calculator()
