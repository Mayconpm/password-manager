import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, width=200, height=200)

canvas = tk.Canvas()
canvas_logo_password = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_logo_password)
canvas.grid(column=0, row=0)
window.mainloop()
