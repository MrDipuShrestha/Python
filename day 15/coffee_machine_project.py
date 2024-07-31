from main import MENU
from main import resources

balance = 0
is_on = True


def is_resource_sufficient(order_ingridient):
    """Return true if there is sufficent ingridients, False if there is not enough ingridients"""
    for item in order_ingridient:
        if order_ingridient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coin():
    """Calculate the total money customer inserted."""
    print("please enter money: ")
    total = int(input("How many Hundred: ")) * 100
    total += int(input("How many Fifty: ")) * 50
    total += int(input("How many Twenty: ")) * 20
    total += int(input("How many Ten: ")) * 10
    total += int(input("How many Five: ")) * 5
    return total


def is_transaction_successful(user_input, ingridient_price):
    """Return True if transaction is successful, False if transaction is unsuccessful"""
    if user_input >= ingridient_price:
        change = round(user_input - ingridient_price, 2)
        print(f"Here is Rs.{change} in change.")
        global balance
        balance += ingridient_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order_name, order_ingridients):
    for item in order_ingridients:
        resources[item] -= order_ingridients[item]
    print(f"Here is your {order_name}. Enjoy!")


while is_on:
    choice = input("What would you like?  (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs.{balance}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
