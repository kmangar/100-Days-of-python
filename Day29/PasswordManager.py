from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_gen():
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split() + "a b c d e f g h i j k l m n o p q r s t u v w x y z".upper().split()
    numbers = "0 1 2 3 4 5 6 7 8 9".split()
    characters = "` ~ ! @ # $ % ^ & * ( ) - _ = + | , . / < > ? ; : '  ".split()

    letter_list = [choice(alphabet) for _ in range(randint(8, 10))]

    char_list = [choice(characters) for _ in range(randint(2, 4))]

    num_list = [choice(numbers) for _char in range(randint(2, 4))]

    password_list = letter_list + char_list + num_list

    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    # IF field is empty promt a messagebox 
    if len(website) <= 1 or len(email) <= 1 or len(password) <= 1:
        messagebox.showinfo(title="OOPS", message="One or more field is empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {email}"
                                                              f"\nPassword: {password}"
                                                              f"\nIs it OK to save? ")
        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    # Read the old data and store it
                    data = json.load(file)
                    # update the old data with the new by adding to it
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
                # with open("data.json", "w") as file:
                #     json.dump(data, file, indent=4)
            finally:
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():

    wesite = website_entry.get()

    try:
        with open("data.json", mode="r") as file:
            # Read the old data and store it
            data = json.load(file)
    except FileNotFoundError :
        messagebox.showinfo(title="OOPS", message="Your password vault is empty")
        # with open("data.json", "w") as file:
        #     json.dump(data, file, indent=4)
    except KeyError:
        messagebox.showinfo(title="OOPS", message="No details for your website exits")
    else:
        print(data[wesite]["email"])

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.config(padx=45, pady=45)
screen.title("Password Manager")
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock = PhotoImage(file='logo.png')

canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", font=("Times New Roman", 12))
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
# sticky accepts compass directions as values, and different combinations of these directions yield different results.
# You can think of sticky as a combination of an alignment and fill option.
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

email_username = Label(text="Email/Username: ", font=("Times New Roman", 12))
email_username.grid(row=2, column=0)

email_username_entry = Entry(width=35)
email_username_entry.grid(columnspan=2, row=2, column=1, sticky="EW")
email_username_entry.insert(0, "khammangar@gmail.com")

password = Label(text="Password: ", font=("Times New Roman", 12))
password.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

generator = Button(text="Generate Password", command=password_gen)
generator.grid(row=3, column=2)

add_button = Button(text="ADD", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

screen.mainloop()
