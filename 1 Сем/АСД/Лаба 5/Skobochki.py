line = input("Введите скобки: ")
cnt = 0
mas = []
if line[0] == ')':
    print('Первый неправильный элемент: 1')
else:
    for i in range(len(line)):
        if line[i] == '(':
            cnt += 1
        elif line[i] == ')':
            cnt -= 1
        else:
            print("Неправильно данные!")
            break
        mas.append(i)
        if cnt < 0:
            print('Первый неправильный элемент: ', i+1)
            break
        elif cnt == 0:
            mas.clear()
    if cnt > 0:
        print('Первый неправильный элемент: ', mas[0]+1)
    elif cnt == 0:
        print("Всё верно!")
