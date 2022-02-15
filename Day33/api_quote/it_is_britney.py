from tkinter import *
import requests
from ApiGetter import ApiGetter

britney = ApiGetter()
# api credit: https://api.britney.rest
britney.api_address = "https://api.britney.rest"

def get_quote():

    canvas.itemconfig(quote_text, text=f"{britney.get_quote()}")


window = Tk()
window.title("britney Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="img/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click britney Get A Quote", width=250, font=("Arial", 24, "bold"), fill="white")
canvas.grid(row=0, column=0)

# img credit: https://favpng.com/
britney_img = PhotoImage(file="img/britney.png")
britney_button = Button(image=britney_img, highlightthickness=0, command=get_quote)
britney_button.grid(row=1, column=0)



window.mainloop()