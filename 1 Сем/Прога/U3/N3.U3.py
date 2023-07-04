a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите третье числоё "))
if a >= b:
    if a > c: print(a)
    else: print(c)
else:
    if b > c: print(b)
    else: print(c)
if a == b and b == c and c == a:
    print("Числа равны")