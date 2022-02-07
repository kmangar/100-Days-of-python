import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    # reset the text to 00:00
    canvas.itemconfig(timer_text, text=f"00:00")

    # title_label reads timer 
    timer_label.config(text="Timer")

    # reset the checkmarks
    check_mark.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS, completed
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    # if it's the 8th REP take long break
    if REPS % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break)
    # if it's the 2nd 4th or 6th take short break
    elif REPS % 2 == 0:
        timer_label.config(text=f"Break", fg=PINK)
        count_down(short_break)
    # If it's the 1st/3rd/5th/7th rep:
    else:
        timer_label.config(text="FOCUS", fg=GREEN)
        count_down(work_sec)
        marks = ""
        completed = math.floor(REPS/ 2)
        for _ in range(completed):
            marks += "✔"
        check_mark.config(text=marks)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45, "bold"), bg=YELLOW, highlightthickness=0)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", bg=GREEN, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=RED, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark.grid(row=3, column=1)

window.mainloop()
