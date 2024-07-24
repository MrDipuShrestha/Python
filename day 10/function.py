# Function with output


def format_name(f_name, l_name):

    # docstring
    """This is function is for the title case of the given name."""

    if f_name == "" or l_name == "":
        return "Enter a valid input."
    firstName = f_name.title()
    lastName = l_name.title()
    # return firstName + " " + lastname
    return f"{firstName} {lastName}"


fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

name = format_name(f_name=fname, l_name=lname)
print(f"Your name is {name}.")
