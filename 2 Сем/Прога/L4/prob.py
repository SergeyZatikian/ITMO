from tkinter import *
mGui = Tk()

number=0
currency=StringVar()
tester=0

def fromNZD():
    global tester
    currencySelect=currency.get()
    if currencySelect ==1:
        tester = 0.4 #eg's
    elif currencySelect ==2:
        tester= 1.2 #eg's

    userInput=number.get()
    final=(float(userInput)*(tester))#<-------
    mlabel2=Label(mGui,text='${0:.2f}!'.format(final)).pack()


def toNZD():
    userInput2=number.get()
    userInput2=(float(userInput2)/0.6)
    mlabel3=Label(mGui,text='${0:.2f}!'.format(userInput2)).pack()

def terminate():
    global mGui
    mGui.destroy()


menu = Menu(mGui)
mGui.config(menu=menu)

tofrom = StringVar(mGui)
tofrom.set("To") #initial value

subMenu = Menu(menu)
menu.add_cascade(label="Currency Settings", menu=subMenu)
subMenu.add_command(label="From NZD", command=fromNZD)
subMenu.add_separator()
subMenu.add_command(label="To NZD", command=toNZD)

editMenu = Menu(menu)
menu.add_cascade(label="Options", menu=editMenu)
editMenu.add_command(label="Exit", command=terminate)

mlabel = Label(text='Currency Calculator',bg="orange red", fg='gray20',font=("Century Gothic",20))
mlabel.pack(fill=X)

Radiobutton(mGui, text="GBP", variable=currency, value=1, indicatoron=0).pack()
Radiobutton(mGui, text="USD", variable=currency, value=2, indicatoron=0).pack()


number=Entry(mGui,textvariable=number)
number.pack(pady=8)

mGui.configure(background='deepskyblue3')
mGui.geometry('450x450+500+300')
mGui.title('Currency Converter')
mGui.mainloop()