def prost(n):
    a = list()
    l = [2]
    for i in range(n):
        k = 0
        for j in l:
            if i % j == 0:
                k = 1
        if k == 0:
            a.append(i)
    return(a)
a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = list()
for i in prost(max(a, b)):
    if i not in prost(min(a, b)): c.append(i)
print(c)