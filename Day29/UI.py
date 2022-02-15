from tkinter import *
from PasswordGenerator import PasswordGen

# ---------------------------- UI SETUP ------------------------------- #
class UI():

    def __init__(self):
        self.generator = PasswordGen()

        self.screen = Tk()
        self.screen.config(padx=45, pady=45)
        self.screen.title("Password Manager")
        self.canvas = Canvas(width=200, height=200, highlightthickness=0)
        self.lock = PhotoImage(file='logo.png')

        self.canvas.create_image(100, 100, image=self.lock)
        self.canvas.grid(row=0, column=1)

        self.website_label = Label(text="Website: ", font=("Times New Roman", 12))
        self.website_label.grid(row=1, column=0)

        self.website_entry = Entry(width=35)
        # sticky accepts compass directions as values, and different combinations of these directions yield different
        # results. You can think of sticky as a combination of an alignment and fill option.
        self.website_entry.grid(columnspan=2, row=1, column=1, sticky="EW")
        self.website_entry.focus()

        self.email_username = Label(text="Email/Username: ", font=("Times New Roman", 12))
        self.email_username.grid(row=2, column=0)

        self.email_username_entry = Entry(width=35)
        self.email_username_entry.grid(columnspan=2, row=2, column=1, sticky="EW")
        self.email_username_entry.insert(0, "test@gmail.com")

        self.password = Label(text="Password: ", font=("Times New Roman", 12))
        self.password.grid(row=3, column=0)

        self.password_entry = Entry(width=21)
        self.password_entry.grid(row=3, column=1, sticky="EW")

        self.generator = Button(text="Generate Password", command=self.generator.password_gen)
        self.generator.grid(row=3, column=2)

        self.add_button = Button(text="ADD", width=36, command=save_password)
        self.add_button.grid(row=4, column=1, columnspan=2)
        self.screen.mainloop()