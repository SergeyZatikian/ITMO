def binSearch(a, k, cnt=0):
    min, max = 0, len(a)-1
    cnt += 1
    i = (min + max)//2
    cel = a[i]
    while cel != k:
        if cel > k:
            cnt += 1
            max = i - 1
            i = (max + min)//2
            cel = a[i]
        elif cel < k:
            cnt += 1
            min = i + 1
            i = (max + min)//2
            cel = a[i]
    print("Ваше число под номером ",i+1)
    print("Число итераций", cnt)
a=[]
n = int(input("Введите длину массива: "))
print("Введите подряд все элементы")
for i in range(n):
    a.append(int(input()))
print("Введите загаданное число из данного списка ")
k = int(input())
binSearch(a, k)
