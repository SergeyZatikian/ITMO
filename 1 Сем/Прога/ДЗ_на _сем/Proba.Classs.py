import datetime
import codecs
import string

'''
class goods:
    def __main__(self):
        self.goods = []
'''
self = list()
def add(self):
    try:
        day, month, year = list(int, input("Введите дату (день, месяц и число 01.01.2001) ").split('.'))
        date = datetime.date(year, month, day)
        kateg = input("Введите категорию товаров ")
        name = input("Введите наименование товара ")
        price = int(input("Введите цену товара "))
        cnt = int(input("Введите количестов товаров "))
        if price <= 0 or cnt < 1:
            print("Неверный ввод данных")
        else:
            cost = price * cnt
            self = ([date, kateg, name, price, cnt, cost])
            back = input("Отменить добавление да/нет ")
            if back == 'Да' or back == 'да':
                self.pop(-1)
    except:
        print("Неверный ввод данных ")

def empty(self):
    if len(self) == 0:
        return True 
    return False

def delete(self):
    if self.empty() == True:
        print("Список пуст")
    else:
        info = input("Выберите параметр поиска (дата/категория/наименование/цена/количество/стоимость) ")
        if info not in ('дата','категория','наименование','цена','количество','стоимость'):
            print("Неправильный параметр поиска ")
        else:
            try:
                if info == 'дата':
                    num = 6
                    day, month, year_= map(int, input('Введите дату покупки: ').split('.'))
                    info = datetime.date(year_, month, day)
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
                for elem in self:
                    if info == elem[num]:
                        print('Дата:', elem[0].day, elem[0].month, elem[0].year, 'категория:', elem[1], 'наименование:', elem[2],
                              'цена:', elem[3], 'количесвто:', elem[4], 'стоимость:', elem[5])
                        answer = input("Это искомая запись (да/нет) ")
                        if answer == 'да':
                            self.remove(elem)
                            info = None
                            break
                if info != None:
                    print("Продукта с веденной информацией нет ")
                else:
                    print("Запись успешно удалена ")
            except:
                print('Неверно введено значение параметра поиска')

def sortong(self):
    if self.empty() == True:
        print('Список пуст')
    else:
        back = input("Отменить сортировку (да/нет) ")
        if back == 'нет':
            parametr = input("По какому параметру сортировать ('дата','категория','наименование','цена','количество','стоимость'): ")
            if parametr not in ('дата','категория','наименование','цена','количество','стоимость'):
                print('Неправельный параметр ')
            else:
                if parametr == 'дата':
                    self = sorted(self, key=lambda x: x[0])
                elif parametr == 'категория':
                    self = sorted(self, key=lambda x: x[1])
                elif parametr == 'наименование':
                    self = sorted(self, key=lambda x: x[2])
                elif parametr == 'цена':
                    self = sorted(self, key=lambda x: x[3])
                elif parametr == 'количество':
                    self = sorted(self, key=lambda x: x[4])
                elif parametr == 'стоимость':
                    self = sorted(self, key=lambda x: x[5])
                vozr = input('Сортировать по возрастанию (да/нет) ')
                if vozr == 'нет':
                    self = self[::-1]

def printing(self):
    if self.empty() == True:
        print('Список пуст ')
    else:
        for elem in self:
            print('Дата:', str(elem[0].day) + '.' + str(elem[0].month) + '.' + str(elem[0].year), 'Категория:', elem[1], 'Наименование:', elem[2],
            'Цена:', elem[3], 'Количесвто:', elem[4], 'Стоимость:', elem[5])
list_goods = list()

with codecs.open("C:\\Users\\36050\\OneDrive\\Рабочий стол\\Прога\\ДЗ_на _сем\\data.txt", 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        data = list(map(str, f.readline().split()))
        list_goods.extend([datetime.date(int(data[2]), int(data[1]), int(data[0])), data[3], data[4], int(data[5]), int(data[6]), int(data[7])])
    print(n)
while True:
    command = input('Выберете команду: \nвыйти\nдобавить\nудалить\nпочистить список\nотстортировать\nпросмотреть все записи\n')
    if command == 'добавить':
        list_goods.add()
    elif command == 'удалить':
        list_goods.delete()
    elif command == 'очистить список':
        list_goods.clear()
    elif command == 'отстортировать':
        list_goods.sorting()
    elif command == 'просмотреть все записи':
        list_goods.printing()
    elif command == 'выйти':
        break
    else:
        print('Неверная команда')

with codecs.open("data.txt", 'w', 'utf-8-sig') as f:
    f.write(str(len(list_goods)) + '\n')
    for elem in list_goods:
        f.write(str(elem[8].day) + ' ' + str(elem[0].month) + ' ' + str(elem[0].year) + ' ' + str(elem[1])
                + ' ' + str(elem[2]) + ' ' + str(elem[3]) + ' ' + str(elem[4]) + ' ' + str(elem[5]) + '\n')