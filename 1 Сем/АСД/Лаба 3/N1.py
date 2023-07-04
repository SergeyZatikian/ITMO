from random import randint
 
cnt, a = 10, []
for i in range(cnt):
    a.append(randint(1, 99))
print(a)
 
for i in range(cnt-1):
    for j in range(cnt-i-1):
        if a[j] > a[j+1]: a[j], a[j+1] = a[j+1], a[j]
print(a)