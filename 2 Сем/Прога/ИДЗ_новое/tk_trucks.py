from main import Trucks
from all_trucks import all_trucks
from tkinter import *
from db_Trucks import DataBase
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk 
from ttkthemes import ThemedTk ,ThemedStyle, THEMES


def adding_car():
    data = []
    for i in base.get_all_cars():
        data.append(int(i[0]))
    num, name, weight = max(data) + 1, name_enter.get(), weight_enter.get()
    if not str(weight).isdigit():
        messagebox.showerror('Удаление', 'Неверные данные!')
    if len(name) > 30:
        messagebox.showerror('Удаление', 'Слишком длинное имя!')
    elif int(weight) > 1000000 or int(weight) <= 0:
        messagebox.showerror('Удаление', 'Некорректная грузоподъёмность!')
    else:
        car1 = Trucks(num, name, int(weight))
        base.add_cars(car1)
        messagebox.showinfo('Добавление', 'Транспорт добавлен!')


def delete_car():
    try:
        base.del_cars(int(num_enter.get()))
        messagebox.showinfo('Удаление', 'Транспорт удалён!')
    except Exception:
        messagebox.showerror('Удаление', 'Неверный номер!')


def show_all():
    data = base.get_all_cars()
    string = 'номер, имя, грузоподъёмность, статус \n'
    for i in data:
        for j in i:
            string += str(j) + ', '
        string += '\n'
    messagebox.showinfo('Транспорт', string)


def show_range():
    data = base.get_range_cars()
    string = 'номер, имя, грузоподъёмность, статус \n'
    for i in data:
        for j in i:
            string += str(j) + ', '
        string += '\n'
    messagebox.showinfo('Транспорт', string)


def show_free():
    data = base.get_free_cars()
    if len(data) == 0:
        string = 'Таких машин на данный момент нет!'
    else:
        string = 'номер, имя, грузоподъёмность, статус \n'
        for i in data:
            for j in i:
                string += str(j) + ', '
            string += '\n'
    messagebox.showinfo('Транспорт', string)


def show_busy():
    data = base.get_busy_cars()
    if len(data) == 0:
        string = 'Таких машин на данный момент нет!'
    else:
        string = 'номер, имя, грузоподъёмность, статус \n'
        for i in data:
            for j in i:
                string += str(j) + ', '
            string += '\n'
    messagebox.showinfo('Транспорт', string)


def show_available():
    try:
        if int(weight_sel_enter.get()) > 1000 or int(weight_sel_enter.get()) < 0:
            raise Exception
        data = base.get_available_cars(int(weight_sel_enter.get()))
        string = 'номер, имя, грузоподъёмность, статус \n'
        for i in data:
            for j in i:
                string += str(j) + ', '
            string += '\n'
        messagebox.showinfo('Транспорт', string)
    except Exception:
        messagebox.showerror('Транспорт', 'Неверная грузоподъёмность!')


def booking():
    try:
        flg = base.book_current_car((int(num_book_enter.get())))
        if flg:
            messagebox.showinfo('Удаление', 'Транспорт забронирован!')
        else:
            messagebox.showerror('Удаление', 'Неверный номер!')
    except Exception as error:
        messagebox.showerror('Удаление', 'Неверный номер!')


def exit_app():
    window.quit()


base = all_trucks()
window = Tk()
window.title("Грузовичков")
window.geometry('488x315')
window.resizable(False, False)
style = ThemedStyle(window)
style.set_theme("scidpurple")

adding_lbl = Label(window, text="Добавление транспорта", font=("Arial Bold", 10))  # создаём блок с добавлением транспорта
adding_lbl.place(relx=0.0, rely=0.00)

name_lbl = Label(window, text="Название машины:", font=("Arial Bold", 10))
name_lbl.place(relx=0.0, rely=0.07)
name_enter = ttk.Entry(window, width=10)
name_enter.place(relx=0.25, rely=0.07)

weight_lbl = Label(window, text="Грузоподъёмность:", font=("Arial Bold", 10))
weight_lbl.place(relx=0, rely=0.16)
weight_enter = ttk.Entry(window, width=10)
weight_enter.place(relx=0.25, rely=0.16)

adding_btn = ttk.Button(window, text="Добавить",width=29, command=adding_car)
adding_btn.place(relx=0.01 ,rely=0.25 )


del_lbl = Label(window, text="Удаление транспорта",
                font=("Arial Bold", 10))  # создаём блок с удалением транспорта
del_lbl.place(relx=0.5, rely=0.0)

num_lbl = Label(window, text="Номер машины:", font=("Arial Bold", 10))
num_lbl.place(relx=0.5, rely=0.07)

num_enter = ttk.Entry(window, width=10)
num_enter.place(relx=0.705, rely=0.07)

delete_btn = ttk.Button(window, text="Удалить", width=26, command=delete_car)
delete_btn.place(relx=0.5, rely=0.16)

all_cars_lbl = Label(window, text="Показать все машины:", font=("Arial Bold", 10))             # создаём вывод всех машин
all_cars_lbl.place(relx=0, rely=0.35)

all_cars_btn = ttk.Button(window, text="Вывести", command=show_all)
all_cars_btn.place(relx=0.29, rely=0.35)

range_cars_lbl = Label(window, text="Показать машины \n  по грузоподъёмности:", font=("Arial Bold", 10))             # создаём вывод машин по грузоподъёмености
range_cars_lbl.place(relx=0.5, rely=0.35)

range_cars_btn = ttk.Button(window, text="Вывести", command=show_range)
range_cars_btn.place(relx=0.8, rely=0.365)


free_cars_lbl = Label(window, text="Показать свободные машины:", font=("Arial Bold", 10))             # создаём вывод свободных машин
free_cars_lbl.place(relx=0, rely=0.47)

free_cars_btn = ttk.Button(window, text="Вывести", command=show_free)
free_cars_btn.place(relx=0.38, rely=0.47)


busy_cars_lbl = Label(window, text="Показать занятые машины:", font=("Arial Bold", 10))             # создаём вывод занятых машин
busy_cars_lbl.place(relx=0.5, rely=0.47)

busy_cars_btn = ttk.Button(window, text="Вывести", command=show_busy)
busy_cars_btn.place(relx=0.85, rely=0.47)


select_lbl = Label(window, text="Подбор транспорта:", font=("Arial Bold", 10))  # создаём блок с подбором транспорта
select_lbl.place(relx=0.08, rely=0.56)

weight_sel_lbl = Label(window, text="Грузоподъёмность:", font=("Arial Bold", 10))
weight_sel_lbl.place(relx=0, rely=0.65)

weight_sel_enter = ttk.Entry(window, width=10)
weight_sel_enter.place(relx=0.25, rely=0.65)

select_btn = ttk.Button(window, text="Подобрать", width=30, command=show_available)
select_btn.place(relx=0, rely=0.74)


book_lbl = Label(window, text="Бронирование транспорта:", font=("Arial Bold", 10))  # создаём блок с бронированием транспорта
book_lbl.place(relx=0.5, rely=0.56)

num_book_lbl = Label(window, text="Номер:", font=("Arial Bold", 10))
num_book_lbl.place(relx=0.55, rely=0.65)

num_book_enter = ttk.Entry(window, width=10)
num_book_enter.place(relx=0.65, rely=0.65)

book_btn = ttk.Button(window, text="Забронировать", width=18, command=booking)
book_btn.place(relx=0.55, rely=0.74)


exit_btn = ttk.Button(window, text="Выход", command=exit_app)
exit_btn.place(relx=0.9, rely=0.9)

window.mainloop()
