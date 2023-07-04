raz, sliv = [], []
def slian(first, second):
    global sliv
    new_arr = []
    a = 0
    b = 0
    while a < len(first) and b < len(second):
        if first[a] <= second[b]:
            new_arr.append(first[a])
            a += 1
        else:
            new_arr.append(second[b])
            b += 1
    itog = new_arr + first[a:] + second[b:]
    sliv.append(itog)
    return itog


def merge_sort(data):
    global raz
    if len(data) <= 1:
        return data
    else:
        middle = len(data) // 2
        left, right = data[:middle], data[middle:]
        raz.append(left)
        raz.append(right)
        print(left, right)
        return slian(merge_sort(left), merge_sort(right))


arr = [1,7,15,18,22,19,9,8]
n = len(arr)
merge_sort(arr)
print('разбиение')
print(raz[0], raz[1])
curr = 2
razmer = 2
flag = True
while True:
    if not flag:
        break
    for i in range(razmer):
        print(raz[curr], raz[curr + (n - 2)], end=' ')
        curr += 1
        if curr == n:
            flag = False
            break
    print()
    razmer *= 2

print('слияние')
flag = False
for razm in range(2, n + 1):
    for elem in sliv:
        if len(elem) == razm:
            flag = True
            print(elem, end=" ")
    if flag:
        print()
        flag = False
