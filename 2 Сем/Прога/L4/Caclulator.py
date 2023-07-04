from string import ascii_lowercase, ascii_uppercase, digits, punctuation

import tkinter as tk

from PIL import Image

import customtkinter as CTk


class App(CTk.CTk):

    CTk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    CTk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
    
    def __init__(self):
        super().__init__()

        text = "Hello!"

        self.geometry("820x370")
        self.title("Калькулятор")
        self.resizable(False, False)


        self.textbox = CTk.CTkTextbox(self, width=250)
        self.sidebar_frame = CTk.CTkFrame(self, width=140, corner_radius=0)

        self.button = CTk.CTkButton(master=self, text="CTkButton", command=self.button_function)  # кнопка
        self.button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        
        self.button_exit = CTk.CTkButton(self, text="Закрыть окно", command=self.quit)  # кнопка
        self.button_exit.place(relx=0.91, rely=0.95, anchor=tk.CENTER)


        self.radiobutton_frame = CTk.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tk.IntVar(value=0)
        self.label_radio_group = CTk.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = CTk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = CTk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = CTk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.settings_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.settings_frame.grid(row=1, column=0, sticky="nsew")

        self.appearance_mode_option_menu = CTk.CTkOptionMenu(self.settings_frame,
                                                             values=["Умножить", "Поделить"],
                                                             )
        self.appearance_mode_option_menu.grid(row=0, column=0, columnspan=2, pady=(0, 0))

        self.all_info_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.all_info_frame.grid(row=0, column=0, sticky="news")
        # self.all_info_frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)



 



    def button_function(self):
        print("button pressed")

    def change_appearance_mode_event(self, new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    def truck_info(self, truck_name):
        for i in range(len(self.show_message()[1])):
            if self.show_message()[1][i] == truck_name:
                print(self.show_message()[0][i])

                label = CTk.CTkLabel(master=self, text=self.show_message()[0][i], width=120, height=25, text_color="gray", font=('Courier',14),  corner_radius=8)
                label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)



if __name__ == "__main__":
    app = App()
    app.mainloop()