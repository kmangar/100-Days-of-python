import json
from tkinter import *
from tkinter import messagebox
import UI

# ---------------------------- SAVE PASSWORD ------------------------------- #
class Saver():

    def __init__(self):
        self.password_entry = UI.password_entry
        self.website_entry = UI.website_entry
        self.email_username_entry = UI.email_username_entry


    def save_password(self):

        website = self.website_entry.get()
        email = self.email_username_entry.get()
        password = self.password_entry.get()

        new_data = {
            website: {
                "email: ": email,
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
                    self.website_entry.delete(0, END)
                    self.password_entry.delete(0, END)