def inp(a, k, b):
    i = 0
    while (len(a) > 1):
        for j in range(k - 1):
            i = (i + 1)%len(a)
        a.pop(i)
        b.pop(i)
        if (i > len(a) - 1):
            i = 0
        for h in range(len(a)):
            a[i] = h + 1
            i = (i + 1) % len(a)
    return b[0]

k = 16
print("Введите количество человек: ")
n = int(input())
a = []
b = []
for i in range(n):
    a.append(i + 1)
    b.append(i + 1)

print(inp(a, k, b))