def Average(t):
    i = 0
    summ = 0
    while i < len(t):
        if (t[i] == "None"):
            t.pop(i)
        else:
            summ += t[i]
            i += 1

    return (summ/len(t))

print("Введите список температур (чтобы закончить введите q): ")
s = ""
t = []
while (s != "q"):
    s = input("Введите значение температуры: ")
    if (s != "q") and (s != "None"):
        t.append(int(s))
    elif (s == "None"):
        t.append(s)

print(Average(t))