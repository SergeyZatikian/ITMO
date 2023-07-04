a = int(input("Введите порядковый номер месяца "))
if a > 0 and a < 13:
    if a in [1, 2, 13]:
        print("Зима")
    elif a in [3, 4, 5]:
        print("Весна")
    elif a in [6, 7, 8]:
        print("Лето")
    else:
        print("Осень")
else:
    print("Такого месяца нет")