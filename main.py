import json
import string
import tkinter as tk
from random import choice, randint, shuffle
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list(string.ascii_letters)
    numbers = [str(number) for number in range(0, 10)]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_list += [choice(letters) for char in range(nr_letters)]

    password_list += [choice(symbols) for char in range(nr_symbols)]

    password_list += [choice(numbers) for char in range(nr_numbers)]

    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, "end")
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {"email": email, "password": password},
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty field", message="We cannot save with a empty field, check your data.")
        save = False
    else:
        save = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered\nEmail: {email}\nPassword: {password}\nIs is ok to save?",
        )

        if save:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, "end")
                password_input.delete(0, "end")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_input.get()
    if len(website) == 0:
        messagebox.showinfo(title="Empty field", message="We cannot search without a website.")
        save = False
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Website error", message="We cannot find that for that website.")
        else:
            if website in data:
                website_data = data[website]
                email = website_data["email"]
                password = website_data["password"]
                messagebox.showinfo(
                    title=website,
                    message=f"Email: {email}\nPassword: {password}",
                )
                pyperclip.copy(password)
            else:
                messagebox.showinfo(title="Website error", message=f"{website} is not in the database.")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
canvas_logo_password = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_logo_password)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website: ")
website_label.grid(column=0, row=1)

website_input = tk.Entry(width=34)
website_input.focus()
website_input.grid(column=1, row=1)

password_button = tk.Button(text="Search", command=search_password, width=15)
password_button.grid(column=2, row=1)

email_label = tk.Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_input = tk.Entry(width=53)
email_input.insert(0, "dummy.test@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

password_label = tk.Label(text="Password: ")
password_label.grid(column=0, row=3)

password_input = tk.Entry(width=34)
password_input.grid(column=1, row=3, sticky="e", padx=2)

password_button = tk.Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=45, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
