def func1(x, y):
    pr = 1
    for i in range(y):
        pr *= x
    return pr

def func2(x, y, pr):
    if y <= 0:
        return pr
    else:
        return func2(x, y - 1, pr*x)

print(func1(2, 0))    #Вызываем функцию func1
print(func2(2, 0, 1))    #Вызываем функцию func2
