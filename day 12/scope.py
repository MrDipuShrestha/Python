############ sccope ############

name = "Dipesh"  # global  scope variable


def person():
    def profile():
        age = 20  # local scope variable
        print(f"My name is {name} and i am {age} years old.")

    profile()


person()

# using global keywrod you can access global variable inside the local block

age = 20


def profile():
    global age
    print(f" i am {age} years old.")


profile()


# using this you can modify global variable
age = 20


def profile():
    print(f" i am {age} years old.")
    return age + 1


age = profile()
print(age)


# global constant

# write constant variable in upper case
PI = 3.14159
URL = "https://www.google.com"


def calc():
    print(PI)
