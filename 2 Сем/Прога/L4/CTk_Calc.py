import tkinter as tk
import customtkinter as CTk
from tkinter import *
from tkinter import messagebox
import math

class App(CTk.CTk):

    CTk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    CTk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


    def __init__(self):
        super().__init__()

        self.geometry("520x370")
        self.title("Калькулятор")
        self.resizable(True, True)

        main_menu = Menu()
        self.option_add("*tearOff", FALSE)
        file_menu = Menu()
        file_menu.add_separator()
        file_menu.add_command(label="Exit")

        Opt = Menu()
        Opt.add_command(label="+")
        Opt.add_command(label="-")
        Opt.add_command(label="*")
        Opt.add_command(label="/")
        Opt.add_command(label="clear")
        
        main_menu.add_cascade(label="Файл", menu=file_menu)
        main_menu.add_cascade(label="Операции", menu = Opt)
        main_menu.add_cascade(label="Справка")
        self.config(menu=main_menu)




        # self.Vibor_Rejima = CTk.CTkFrame(self, fg_color="transparent")
        # self.Vibor_Rejima.grid(row=5, column=5, sticky="nsew")
        self.radio_var = tk.IntVar(value=0)
        self.radio_button_1 = CTk.CTkRadioButton(master=self, text="Калькулятор", variable=self.radio_var, value=0, command=self.all_calc)
        self.radio_button_1.grid(row=0, column=0, sticky="n")
        self.radio_button_1.place(relx=0, rely=0)
        self.radio_button_2 = CTk.CTkRadioButton(master=self, text="Площадь", variable=self.radio_var, value=1, command=self.dest)
        self.radio_button_2.grid(row=1, column=0, sticky="n")
        self.radio_button_1.place(relx=0, rely=0.07)

    def dest(self):
        self.all.destroy()


    def all_calc(self):
        
        self.all = CTk.CTkFrame(master=self, width=450, height=400, fg_color="red")
        self.all.grid(row=0, column=0, pady=40, padx=40, ipadx = 20, ipady = 20, sticky="news")
        self.calc = CTk.CTkEntry(self.all, font=('Times New Roman', 15), width=180, height=23)
        # self.calc.insert(0, '0')
        self.calc.place(relx=0.2, rely=0.001)
        self.make_digit_button('1').place(relx = 0.2,  rely = 0.4)
        self.make_digit_button('2').place(relx = 0.3,  rely = 0.4)
        self.make_digit_button('3').place(relx = 0.4,  rely = 0.4)
        self.make_digit_button('4').place(relx = 0.2,  rely = 0.3)
        self.make_digit_button('5').place(relx = 0.3,  rely = 0.3)
        self.make_digit_button('6').place(relx = 0.4,  rely = 0.3)
        self.make_digit_button('7').place(relx = 0.2,  rely = 0.2)
        self.make_digit_button('8').place(relx = 0.3,  rely = 0.2)
        self.make_digit_button('9').place(relx = 0.4,  rely = 0.2)
        self.zer('0').place(relx = 0.2,  rely = 0.5)
        self.make_digit_button('.').place(relx = 0.4,  rely = 0.5)

        #Основные математические действия
        self.make_operation_button('+').place(relx = 0.5,  rely = 0.5)
        self.make_operation_button('-').place(relx = 0.5,  rely = 0.4)
        self.make_operation_button('*').place(relx = 0.5,  rely = 0.3)
        self.make_operation_button('/').place(relx = 0.5,  rely = 0.2)

        #Корень
        self.make_prob('').place(relx = 0.3,  rely = 0.1)

        #Модуль
        self.make_fabs_button().place(relx = 0.4,  rely = 0.1)

        #Кнопка очистки
        self.make_clear_button().place(relx = 0.2, rely = 0.1)

        #Равно
        self.make_calc_button().place(relx = 0.5,  rely = 0.1)


    def button_function(self):
        print("button pressed")

    def change_appearance_mode_event(self, new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    def add_digit(self, digit):
        value = self.calc.get()
        if value[0]=='0' and len(value)==1:
            value = value[1:]
        self.calc.delete(0, END)
        self.calc.insert(0, value + digit)

    def add_operation(self, operation):
        value = self.calc.get()
        if value[-1] in '-+/*':
            value = value[:-1]
        elif '+' in value or '-' in value or'*' in value or'/' in value:
            self.calculate()
            value = self.calc.get()
        self.calc.delete(0, END)
        self.calc.insert(0, value + operation)

    def calculate(self):
        value = self.calc.get()
        if value[-1] in '-+/*':
            value = value+value[:-1]
        self.calc.delete(0, END)
        try:
            self.calc.insert(0, eval(value))
        except (NameError, SyntaxError):
            messagebox.showinfo('Внимание!', 'Нужно вводить только числа!')
            self.calc.insert(0, 0)
        except ZeroDivisionError:
            messagebox.showinfo('Внимание!', 'На ноль делить нельзя!')
            self.calc.insert(0, 0)

    def add_sqrt(self):
        value = self.calc.get()
        value = float(value)
        value = math.sqrt(value)
        self.calc.delete(0, END)
        self.calc.insert(0, value)
        

    def add_fabs(self):
        value = self.calc.get()
        value = eval(value)
        value = math.fabs(value)
        self.calc.delete(0, END)
        self.calc.insert(0, value)
            
    def clear(self):
        self.calc.delete(0, END)
        self.calc.insert(0, 0)

    def make_calc_button(self):
        return CTk.CTkButton(self.all, text='=', width=45, height=35, font=('Times New Roman', 20),command=self.calculate)

    def make_clear_button(self):
        return CTk.CTkButton(self.all, text='C', width=45, height=35, font=('Times New Roman', 20), command=self.clear)

    def make_operation_button(self,operation):
        return CTk.CTkButton(self.all, text=operation, width=45, height=35, font=('Times New Roman', 20), command=lambda : self.add_operation(operation))

    def make_fabs_button(self):
        return CTk.CTkButton(self.all, text="|x|", width=45, height=35, font=('Times New Roman', 20), command=self.add_fabs)

    def make_digit_button(self, digit):
        return CTk.CTkButton(self.all, text=digit, width=45, height=35, font=('Times New Roman', 20), command=lambda : self.add_digit(digit))
    # img = PhotoImage(file="./img/back-button.png")
    # def make_sqrt(self):
    #     img = PhotoImage(file="sqrt.jpg")
        return CTk.CTkButton(master = self, image = img, width=45, height=35, font=('Times New Roman', 20))
    def make_prob(self, digit):
        return CTk.CTkButton(self.all, text=digit, width=45, height=35, font=('Times New Roman', 20), command=self.add_sqrt)
    def zer(self, digit):
        return CTk.CTkButton(self.all, text=digit, width=97, height=35, font=('Times New Roman', 20), command=lambda : self.add_digit(digit))

if __name__ == "__main__":
    app = App()
    app.mainloop()