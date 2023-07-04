a = input("Введите имя ")
b = input("Введите время ")
d = list(map(int, b.split(":")))
b = d[0]
if b < 25:
    if b >= 6 and b <= 12:
        print("Доброе утро " + a)
    elif b >= 12 and b < 19:
        print("Добрый день " + a)
    elif (b >= 19 and b <= 23):
        print("Добрый вечер " + a)
    else:
        print("Доброй ночи " + a)
else: 
    print("Нет такого врмемени ")