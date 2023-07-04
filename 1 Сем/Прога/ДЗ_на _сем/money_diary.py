list_goods = []

def add(goods):
    try:
        date = input("Введите дату (день, месяц и число 01.01.2001) ")
        kateg = input("Введите категорию товаров ")
        name = input("Введите наименование товара ")
        price = int(input("Введите цену товара "))
        cnt = int(input("Введите количестов товаров "))
        if price <= 0 or cnt < 1:
            print("Неверный ввод данных")
        else:
            cost = price * cnt
            goods = ([date, kateg, name, price, cnt, cost])
            back = input("Отменить добавление да/нет ")
            if back == 'нет' or back == 'Нет':
                list_goods.append(goods)
    except:
        print("Неверный ввод данных ")

def empty(goods):
    if len(goods) == 0:
        return True 
    return False

def printing(goods):
    if empty(goods) == True:
        print('Список пуст ')
    else:
        for elem in goods:
            print('Дата:',elem[0], 'Категория:', elem[1], 'Наименование:', elem[2],
            'Цена:', elem[3], 'Количесвто:', elem[4], 'Стоимость:', elem[5])

def sortong(goods):
    if empty(goods) == True:
        print('Список пуст')
    else:
        back = input("Отменить сортировку (да/нет) ")
        if back == 'нет':
            parametr = input("По какому параметру сортировать ('дата','категория','наименование','цена','количество','стоимость'): ")
            if parametr not in ('дата','категория','наименование','цена','количество','стоимость'):
                print('Неправельный параметр ')
            else:
                global list_goods
                if parametr == 'дата':
                    list_goods = sorted(goods, key=lambda x: x[0])
                elif parametr == 'категория':
                    list_goods = sorted(goods, key=lambda x: x[1])
                elif parametr == 'наименование':
                    list_goods = sorted(goods, key=lambda x: x[2])
                elif parametr == 'цена':
                    list_goods = sorted(goods, key=lambda x: x[3])
                elif parametr == 'количество':
                    list_goods = sorted(goods, key=lambda x: x[4])
                elif parametr == 'стоимость':
                    list_goods = sorted(goods, key=lambda x: x[5])
                vozr = input('Сортировать по возрастанию (да/нет) ')
                if vozr == 'нет':
                    list_goods = list_goods[::-1]


def delete(goods):
    if empty(goods) == True:
        print("Список пуст")
    else:
        info = input("Выберите параметр поиска (дата/категория/наименование/цена/количество/стоимость) ")
        if info not in ('дата','категория','наименование','цена','количество','стоимость'):
            print("Неправильный параметр поиска ")
        else:
            try:
                if info == 'дата':
                    num = 0
                    info = input('Введите дату покупки: ')
                elif info == 'категория':
                    num = 1
                    info = input('Введите категорию товара: ')
                elif info == 'наименование':
                    num = 2
                    info = input('Введите  наименование товара: ')  
                elif info == 'цена':
                    num = 3
                    info = int(input('Введите цену товара: '))
                elif info == 'количество':
                    num = 4
                    info = int(input('Введите количество тоавра: '))
                else:
                    num = 5
                    info = int(input('Введите стоимость товара: '))
                for elem in goods:
                    if info == elem[num]:
                        print('Дата:', elem[0], 'категория:', elem[1], 'наименование:', elem[2],
                              'цена:', elem[3], 'количесвто:', elem[4], 'стоимость:', elem[5])
                        answer = input("Это искомая запись (да/нет) ")
                        if answer == 'да':
                            goods.remove(elem)
                            info = None
                            break
                if info != None:
                    print("Продукта с веденной информацией нет ")
                else:
                    print("Запись успешно удалена ")
            except:
                print('Неверно введено значение параметра поиска')



with open("C:\\Users\\36050\\OneDrive\\Рабочий стол\\ИТМО\\1 сем\\Прога\\ДЗ_на _сем\\data.txt", 'r') as f:
    n = int(f.readline())
    for i in range(n):
        data = list(map(str, f.readline().split()))
        list_goods.append([data[0], data[1], data[2], int(data[3]), int(data[4]), int(data[5])])

while True:
    command = input('Выберете команду: \nвыйти\nдобавить\nудалить\nпочистить список\nотсортировать\nпросмотреть все записи\n')
    if command == 'добавить' or command == '1':
        add(list_goods)
    elif command == 'удалить' or command == '2':
        delete(list_goods)
    elif command == 'очистить список' or command == '3':
        list_goods.clear()
    elif command == 'отсортировать' or command == '4':
        sortong(list_goods)
    elif command == 'просмотреть все записи' or command == '5':
        printing(list_goods)
    elif command == 'выйти':
        break
    else:
        print('Неверная команда')

with open("C:\\Users\\36050\\OneDrive\\Рабочий стол\\ИТМО\\1 сем\\Прога\\ДЗ_на _сем\\data.txt", 'w') as f:
    f.write(str(len(list_goods)) + '\n')
    for elem in list_goods:
        f.write(str(elem[0]) + ' ' + str(elem[1])
                + ' ' + str(elem[2]) + ' ' + str(elem[3]) + ' ' + str(elem[4]) + ' ' + str(elem[5]) + '\n')