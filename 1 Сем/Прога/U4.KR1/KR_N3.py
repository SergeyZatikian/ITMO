from random import randint
l = []

pr = list()
porog = int(input())
for i in range(50):
    l.append(randint(1,50))
print(l)
for i in range(len(l)):
    if l[i] > porog:
        pr.append("High")
    elif l[i] < porog:
        pr.append("Low")
    else:
        pr.append("=")
print(pr)
name = "Анна Марк Василиса Мария Захар Вера Михаил Артём Алиса Елена Елизавета Милана Кристина Николай Ярослав София Илья Таисия Иван Алексей Дмитрий Александра Мирослава Кирилл Аделина Даниил Степан Тимур Ева Тигран Григорий Сафия Евгения Сергей Артемий Элина Евгений Данила Арина Фёдор Варвара Герман Маргарита Никита Ольга Ксения Александр Руслан Екатерина Арсений"
name = name.split()
tar1 = "А Б В Г Д Е Ё Ж З И Й К"
tar1 = tar1.split()
print(name)
A = list()
B = list()
a = [i for i in name if i[0] in tar1]
b = [i for i in name if i[0] not in tar1]
print(a, b)