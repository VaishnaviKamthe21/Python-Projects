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
CHECKMARK = "✔"
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    
    global REPS
    REPS += 1
    print(REPS)
    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="Break", fg= RED)
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="Break", fg= PINK)
    else:
        count_down(WORK_MIN * 60)
        title.config(text="Work", fg= GREEN)
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec<10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer() 
        if REPS %2 == 0:
            if REPS % 8 == 0:
                check_marks.config(text="")
            else:
                check_marks.config(text=f"{CHECKMARK * (REPS//2)}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"Python-Projects\pomodoro-start\tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
title = Label(text = "Timer", fg = GREEN, font=(FONT_NAME, 50, "normal"), bg=YELLOW)
title.grid(column=1, row=0)
start_btn = Button(text="Start",highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)
check_marks = Label(text="",fg=GREEN, bg=YELLOW)
check_marks.grid(column=1,row=3)

window.mainloop()