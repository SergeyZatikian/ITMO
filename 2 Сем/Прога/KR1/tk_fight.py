from main import *
from tkinter import *
from main import text
from main import vibor
from tkinter import ttk


def fight():
    global lbl_result
    for i in text:
        lbl_result = Label(window, text=text)
        lbl_result.grid(column=1, row=4)

def clear():
    val2.delete(0, END)
    val1.delete(0, END)
    lbl_result.destroy()

def abc():
    vibor("борьба", "бокс", val1, val2)
    

window = Tk()
window.title("Добро пожаловать в MortalCombatXL")
window.geometry('1000x1000')

lbl = Label(window, text="Привет, это Поединок", font=("Arial Bold", 14))
lbl.grid(column=0, row=0)

lbl1 = Label(window, text="Введите имена: ", font=("Arial Bold", 14))
lbl1.grid(column=0, row=1)

val1 = Entry(window, width=10)
val1.grid(column=1, row=1)
val2 = Entry(window, width=10)
val2.grid(column=2, row=1)


r_var = BooleanVar()
r_var.set(0)
radbutt1 = Radiobutton(window, text='Поединок', variable=r_var, value=0, command=fight)
radbutt1.grid(column=0, row=2)

btn = ttk.Button(text="Button", command=clear)
btn.grid(column=5, row=5)


window.mainloop()