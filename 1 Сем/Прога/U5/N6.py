a = ['k']
while (a[len(a) - 1] != 'Q'):
    a.append(input("Ввеедите элемент: "))
a.pop(0)
a.pop(len(a) - 1)
print(len(a))
for i in range(len(a)):
    a[i] = int(a[i])
print(f"Среднее арифметическое: {sum(a)/len(a)}")
print(f"Сумма: {sum(a)}")
for i in range(len(a)):
    if a[i] == max(a):
        print(f"Максимум {max(a)} с индексом {i}")
        maxi = i
    if a[i] == min(a):
        print(f"Минимум {min(a)} с индексом {i}")
        mini = i
pr = 1
for i in range(min(mini, maxi) + 1, max(mini, maxi)):
    pr *= a[i]
print(f"Произведение: {pr}")