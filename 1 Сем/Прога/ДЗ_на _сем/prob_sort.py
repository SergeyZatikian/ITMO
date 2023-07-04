import codecs

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
                print(list_goods)
                return list_goods

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


list_goods = []

with codecs.open("C:\\Users\\36050\\OneDrive\\Рабочий стол\\Прога\\ДЗ_на _сем\\data.txt", 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        data = list(map(str, f.readline().split()))
        list_goods.append([data[0]+'.'+data[1]+'.'+data[2], data[3], data[4], int(data[5]), int(data[6]), int(int(data[5])*int(data[6]))])

goods = sorted(list_goods, key=lambda x: x[1])
print(goods)


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
        print(list_goods)
    elif command == 'просмотреть все записи' or command == '5':
        printing(list_goods)
    elif command == 'выйти':
        break
    else:
        print('Неверная команда')