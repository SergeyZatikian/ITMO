a = int(input("Введите номер месяца "))
b = int(input("Введите день "))
d = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
sum = d[a]-b
if a > 0 and a < 13 and d[a] >= b:
    for i in range(a, 12):
        sum += d[i]    
    print(sum)
else:
    print("Нет такой даты")