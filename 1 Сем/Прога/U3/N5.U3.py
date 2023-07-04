from random import randint

a = randint(1, 100)
cnt = 10
while cnt != 0:
    c = int(input("Введите число "))
    if a == c: 
        print("Вы угадали") 
        break
    else:
        if a < c: print("Оно меньше вашего")
        else: print("Оно больше вашего")
    cnt -= 1
    if cnt == 0: print("Попытки закончились ")