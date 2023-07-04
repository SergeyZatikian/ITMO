x = int(input("Введите координату по x "))
y = int(input("Введите координату по y "))
if x == 0 and y == 0:
    print("Начало координат")
else:
    if x > 0 and y > 0: print("Первая четверть")
    if x < 0 and y > 0: print("Вторая четверть")
    if x < 0 and y < 0: print("Третья четверть")
    if x > 0 and y < 0: print("Четвертая четверть")
    if x == 0: print("Ось абцисс")
    if y == 0: print("Ось ординат")