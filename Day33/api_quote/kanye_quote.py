from tkinter import *
import requests
from ApiGetter import ApiGetter

kanye = ApiGetter()
kanye.api_address = "https://api.kanye.rest/"

def get_quote():

    canvas.itemconfig(quote_text, text=f"{kanye.get_quote()['quote']}")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="img/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click Kanye Get A Quote", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="img/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()