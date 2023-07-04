a = [195, 200, 154, 176, 172, 187, 184, 197, 199, 193, 140, 163]
answer = True
while (answer):
    height = int(input("Введите рост нового человека: "))
    a.append(height)
    a.sort(reverse=-1)
    print(a)
    for i in range(len(a)):
        if (a[i] == height):
            break
    print(f"Индекс нового человека: {i}")
    k = input("Желаете продолжить? ")
    if (k == "да"): answer = True
    elif (k == "нет"): answer = False