from tkinter import *
import random
ws = Tk()
ws.title('PythonGuides')
ws.geometry('600x400')
ws.config(bg='blue')


ranNum = random.randint(0,10)
chance = 3
var = IntVar()
disp = StringVar()

def check_guess():
    global ranNum
    global chance
    usr_ip = var.get()
    if chance >0:
        if usr_ip == ranNum:
            msg = f"You Won!{ranNum} is the right answer."
        elif usr_ip > ranNum:
            msg = f"{usr_ip} is greahter, you have {chance} chance(s) left"
            chance += 1
        elif usr_ip < ranNum:
            msg = f"{usr_ip} is smaller, you have {chance} chance(s) left"
            chance += 1
        else:
            msg = f"Something went wrong"
    else:
        msg = f"You Lost!{ranNum} is the right answer."
    
    disp.set(msg)

Label(
    ws,
    text = 'Number Guessing Game',
    font = ('sans-serif',20),
    relief = SOLID,
    padx = 10,
    pady = 10,
    bg = 'yellow'
).pack(pady = (10,0))

Entry(
    ws,
    textvariable = var,
    font = ('sans-serif',18),

).pack(pady = (50,10))

Button(
    ws,
    text = "Submit Guess",
    font = ('sans-serif',18),
    command = check_guess
).pack()

Label(
    ws,
    textvariable = disp,
    bg= 'blue',
    fg = 'yellow',
    font = ('sans-serif',22),
).pack(pady = (50,10))

ws.mainloop()