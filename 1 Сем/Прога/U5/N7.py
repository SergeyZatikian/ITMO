
a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''
num = int(input("Введите длину массива: "))
a = []
for i in range(num):
    a.append(int(input("Введите элемент: ")))
'''

n = int(input("Введите число сдвига: "))
if n > len(a):
    print('Error')
else:
    if n > 0:
        for j in range(n):
            k = a[len(a)-1]
            for i in range(len(a)-1, 0, -1):
                a[i] = a[i-1]
            a[0] = k
    elif (n < 0):
        for j in range(abs(n)):
            k = a[0]
            for i in range(len(a)-1):
                a[i] = a[i+1]
            a[len(a)-1] = k
    print(a)