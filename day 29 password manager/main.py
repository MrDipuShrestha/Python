from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import string
import json

{}

FONT = ("Arial", 15)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data:
            {
                "email": email_data,
                "password": password_data,
            }
    }

    if not website_data or not email_data or not password_data:
        messagebox.showwarning(
            title="Missing Information", message="Please don't leave any field empty!"
        )
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search_data():
    try:
        website = website_entry.get()

        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo("File doesn't exist.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]

            messagebox.showinfo(f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(f"The data of {website} doesn't exist.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Use ttk Canvas for logo
canvas = Canvas(window, width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# ttk Label and Entry widgets
website_label = ttk.Label(window, text="Website:", font=FONT)
website_label.grid(row=1, column=0)

website_entry = ttk.Entry(
    window,
    width=35,
)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

search = ttk.Button(window, text="Search", command=search_data)
search.grid(row=1, column=2)

email_label = ttk.Label(window, text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0)

email_entry = ttk.Entry(window, width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "dipesh@gmail.com")

search = ttk.Button(window, text="Search", command=search_data)

password_label = ttk.Label(window, text="Password:", font=FONT)
password_label.grid(row=4, column=0)

password_entry = ttk.Entry(window, width=21)
password_entry.grid(row=4, column=1)

# ttk Button widgets
password_button = ttk.Button(
    window, text="Generate Password", command=generate_password
)
password_button.grid(row=4, column=2)

add_button = ttk.Button(window, text="Add", width=36, command=save_data)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
