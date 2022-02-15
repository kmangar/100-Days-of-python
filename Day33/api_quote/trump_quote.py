from tkinter import *
import requests
from ApiGetter import ApiGetter

trump = ApiGetter()
trump.api_address = "https://api.whatdoestrumpthink.com/api/v1/quotes/random/"

def get_quote():

    canvas.itemconfig(quote_text, text=f"{trump.get_quote()['message']}")


window = Tk()
window.title("Trump Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click trump Get A Quote", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# image credit: https://pngimg.com/image/29355
trump_img = PhotoImage(file="donald_trump.png")
trump_button = Button(image=trump_img, highlightthickness=0, command=get_quote)
trump_button.grid(row=1, column=0)


window.mainloop()