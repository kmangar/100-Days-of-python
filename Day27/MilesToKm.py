from tkinter import *

window = Tk()

window.title("Miles To Km Converter")

window.config(padx=20, pady=20)
miles_input = Entry(width=10)

miles_input.grid(column=1, row=0)
Miles_text = Label(text="Miles")

Miles_text.grid(column=2, row=0)
is_equal = Label(text="is equal to")

is_equal.grid(column=0, row=1)
km_text = Label(text="KM")

km_text.grid(column=2, row=1)
km_output = Label(text="0")

km_output.grid(column=1, row=1)


def conversion():
    miles = int(miles_input.get())
    miles_to_km = miles * 1.609344
    km_output["text"] = f"{round(miles_to_km, 2)}"
    # print(miles_to_km)

calculate = Button(text="Calculate", command=conversion)
calculate.grid(column=1, row=2)
window.mainloop()
