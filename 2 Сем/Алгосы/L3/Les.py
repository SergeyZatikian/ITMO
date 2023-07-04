
mas = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

first = [float("inf"), 0]
for i in mas:
    if i[1] == 0 and i[0] < first[0]:
        first = i

len_mas = len(mas)

new_mas = []
new_mas.append(first)
mas.pop(mas.index(first))
temp = []
while len(new_mas) != len_mas:
    for j in mas:
        l = 0
        for k in range(len(new_mas)):
            if new_mas[k][0] >= j[0]:
                l += 1
        if l == j[1]:
            temp.append(j)
    if len(temp) > 1:
        new_mas.append(min(temp))
    else:
        new_mas.append(temp[0])
    temp = []

print(new_mas)