import math
case = input("Если вы будете вводить равностороний треугольник, напишите цифру 1, инчае 0 ")
if int(case) == 1:
    a = int(input("Введите сторону "))
    p = (a)*3//2
    s = math.sqrt(p*(p-a)**3)
    print("Площадь треугольника = " + str(s))
else:
    print("Введите стороны треугольника")
    a = int(input())
    b = int(input())
    c = int(input())
    if (a+b>c) and (a+c>b) and (b+c>a):
        p = (a+b+c)//2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print("Площадь треугольника = " + str(s))
    else:
        print("Данный треугольник не существует")