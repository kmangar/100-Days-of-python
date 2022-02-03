import pandas
import turtle
import tkinter as tk
import tkinter.messagebox as tkmb
import pandas as pd

def clicked(message):
    for ind, text in enumerate(message):
        # print names in the tkinter window
        # create a label widget
        names_label = tk.Label(window)
        # give it a position using grid
        names_label.grid(row=int(ind)+1, column=0)
        # print the text name in the label
        names_label.config(text=text)


window = tk.Tk()

screen = turtle.Screen()
screen.title("U.S States Guesser")
image = "blank_states_img.gif"
screen.setup(height=491, width=725)
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_correctly = []

while len(guessed_correctly) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_correctly)}/50 Guess A State", prompt="Spell A State: ").title()

    if answer_state == "Exit":
        states_to_learn = []
        for state in all_states:
            if state not in guessed_correctly:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        save = screen.textinput(title=f"SAVE",
                                        prompt="Do you want to save a csv file of missing states? yes or no: ")
        if save.lower() == "yes":
            new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_correctly.append(answer_state)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()

        state_data = data[data.state == answer_state]

        writer.goto(int(state_data.x), int(state_data.y))

        writer.write(answer_state)

# if answer_state
window.title("States Missed:")
btn = tk.Button(window, text="States Missed: ", command=clicked(states_to_learn))

btn.grid(column=0, row=0, padx=30, pady=2)


turtle.mainloop()

# screen.exitonclick()