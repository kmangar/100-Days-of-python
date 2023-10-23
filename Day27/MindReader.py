import tkinter as tk
from time import sleep
from tkinter import *
from tkinter import *
from tkinter.ttk import *
from tkinter import IntVar

window = Tk()

window.title("Mind Reader")

window.config(padx=20, pady=20)

Miles_text = Label(text="Think of a number between 1 and 10:")
Miles_text.grid(column=0, row=0)

miles_input = Entry(width=10)
miles_input.grid(column=0, row=1)

# is_equal = Label(text="is equal to")
#
# is_equal.grid(column=0, row=1)
# km_text = Label(text="is equal to")
#
# km_text.grid(column=2, row=1)
# km_output = Label(text="0")
#
# km_output.grid(column=1, row=1)

#
# def conversion():
#     miles = int(miles_input.get())
#     miles_to_km = miles * 1.609344
#     km_output["text"] = f"{round(miles_to_km, 2)}"
#     # print(miles_to_km)

root = Style()
root.configure("main", title="Mind Reading")


def startReading():
    # The window will stay open until this function call ends.

    sleep(2)  # Replace this with the code you want to run
    root.propagate()
    exit()


calculate = Button(text="Read My Mind", command=startReading)
calculate.grid(column=0, row=2)
window.mainloop()
