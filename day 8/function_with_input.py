#simple function
# def greet():
#     print("Hii..")
#     print("Good Morning")
#     print("What's up?")

# greet()
    
#function with parameter

# def function_with_argument(name):
#     print(f"Hello {name}")
#     print(f"How are you?, {name}")

# function_with_argument(input("Write the name: "))

#function with more than one parameter

def function_with_argument(name,location):
    print(f"Hello {name}")
    print(f"How are you?, {name}")
    print(f"You are from, {location}")

function_with_argument(input("Write the name: "), input("Write location."))