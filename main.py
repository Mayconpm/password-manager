import tkinter as tk
from pathlib import Path

PASSWORD_FILE = "passwords.txt"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    password_line = f"{website} | {email} | {password}\n"
    path = Path(PASSWORD_FILE)

    if path.is_file():
        with open(PASSWORD_FILE, "a") as file:
            file.write(password_line)
    else:
        with open(PASSWORD_FILE, "w") as file:
            file.write(password_line)


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

email_label = tk.Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = tk.Label(text="Password: ")
password_label.grid(column=0, row=3)

website_input = tk.Entry(width=52)
website_input.focus()
website_input.insert(0, "dummy.test@gmail.com")
website_input.grid(column=1, row=1, columnspan=2)

email_input = tk.Entry(width=52)
email_input.grid(column=1, row=2, columnspan=2)

password_input = tk.Entry(width=34)
password_input.grid(column=1, row=3, sticky="e", padx=2)

password_button = tk.Button(text="Generate Password")
password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=45, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
