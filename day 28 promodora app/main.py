from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_job = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Resets the timer and UI elements."""
    if timer_job is not None:
        window.after_cancel(timer_job)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(count_text, text="00:00")
    check_mark.config(text="")

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Starts the timer and alternates between work and break sessions."""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Handles the countdown timer and updates the UI."""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(count_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer_job
        timer_job = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        update_checkmarks()


def update_checkmarks():
    """Updates the checkmarks based on completed work sessions."""
    work_sessions = reps // 2
    check_marks = "✔️" * work_sessions
    check_mark.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
count_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timer.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0, padx=20, pady=20)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2, padx=20, pady=20)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12))
check_mark.grid(row=3, column=1)

window.mainloop()
