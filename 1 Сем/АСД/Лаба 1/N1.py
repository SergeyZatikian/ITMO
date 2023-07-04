def prost(n):
    mas = list()
    for i in range(1, int(n**0.5+1)):
        if n % i == 0: mas.extend([i, n // i])
    return sorted(set(mas))
a = int(input())
n, a, b = 0, 1, 1
if len(prost(a)) == 2:
    print("Простое")
if a == 1:
    print("Фибоначчи")
else:
    while (n <= a + 1):
        a, b = b, (a, b)
        if (n == a):
            print("Фибоначчи")
            break
        else:
            print("не фибоначчи")