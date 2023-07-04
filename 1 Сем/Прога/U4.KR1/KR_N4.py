from random import randint
l = []

pr = list()
for i in range(7):
    l.append(float(input()))
print(l)
for i in range(len(l)):
    if l[i] < 10:
        l[i] *= 1.135
    elif l[i] > 10:
        l[i] *= 0.642
l.sort()
f = open("C:\\Users\\36050\\OneDrive\\Рабочий стол\\Прога\\out.txt", "w")
for i in l:
    print(format(i, '.2f'))
    print(format(i, '.2f'), file = f)
f.close
    