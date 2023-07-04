from abc import abstractmethod
from math import isclose
import sqlite3
import sqlite
class Trucks():
    list_all = []
    def __init__(self, type = 'Null', weight = 'Null', length = "Null", width = "Null", height = "Null", booking = False):
        #         тип грузоподъемность длина ширина высота
        self.type = type
        self.weight = weight
        self.length = length
        self.width = width
        self.heigth = height
        self.booking = booking
        self.all = (type, weight, length, width, height, booking)
        self.list_all.append(self.all)
        #  print(self.list_all , "adf")
        self.__getitem__()
        
    @classmethod
    def __getitem__(cls):
        """Показывает выбранный объект"""
        #i = int(input('Введите число: '))
        # print(cls.list_all)

    def get_all_info(self):
        return(f'Тип: {self.type}, грузоподъемность: {self.weight} т, длина: {self.length} м, ширина: {self.width} м, высота: {self.heigth} м, бронь: {"нет" if self.booking == False else "да"}')

    def get_all(self):
        lis = []
        names = []
        for i in range(len(self.list_all)):
            lis.append(f'Тип: {self.list_all[i][0]}, грузоподъемность: {self.list_all[i][1]} т, длина: {self.list_all[i][2]} м, ширина: {self.list_all[i][3]} м, высота: {self.list_all[i][4]} м, бронь: {"нет" if self.list_all[i][5] == False else "да"}')
            names.append(self.list_all[i][0])
        return [lis, names]
    
    def get_all_names(self):
        lis = []
        for i in range(len(self.list_all)):
            lis.append(self.list_all[i])
        return lis

    def get_all_parametr(self):
        lis = []
        for i in ['тип', 'грузоподъемность', 'длина', 'ширина', 'высота']:
            lis.append(i)
        return lis


    def add_new_Truck(self):
        try:
            self.type = input("Введите тип грузовика: ")
            self.weight = input("Введите грузоподъемность: ")
            self.length = input("Введите длину: ")
            self.width = input("Введите ширину: ")
            self.heigth = input("Введите высоту: ")
        except:
            print("Неправильный ввод данных")
        finally:
            print("Все данные успешно введены")
        pass

    def Sort(self,  parametr):
        sort_list = []
        try:
            if parametr == 'тип':
                sort_list = sorted(self.list_all, key=lambda x: x[0])
            elif parametr == 'грузоподъемность':
                sort_list = sorted(self.list_all, key=lambda x: x[1])
            elif parametr == 'длина':
                sort_list = sorted(self.list_all, key=lambda x: x[2])
            elif parametr == 'ширина':
                sort_list = sorted(self.list_all, key=lambda x: x[3])
            elif parametr == 'высота':
                sort_list = sorted(self.list_all, key=lambda x: x[4])
            elif parametr == 'бронь':
                sort_list = sorted(self.list_all, key=lambda x: x[5])
        except:
            print('Неверно введено значение параметра поиска')
        # print(sort_list)
        return sort_list
            
    def get_booking_info(self, bool):
        for i in self.list_all:
            if i[5] == bool:
                print((f'{i[0]} не забронирован'))
        ans = input("Хотите посмотреть информацию о грузовиках ('да', 'нет'): ")
        if ans == 'да':
            for i in self.list_all:
                if i[5] == bool:
                    return(f'Тип: {i[0]}, грузоподъемность: {i[1]} т, длина: {i[2]} м, ширина: {i[3]} м, высота: {i[4]} м')

    def get_weight_info(self, weight):
        for i in self.list_all:
            if (int(weight) <= int(i[1])):
                return(f'Тип: {i[0]}, грузоподъемность: {i[1]} т, длина: {i[2]} м, ширина: {i[3]} м, высота: {i[4]} м')

    def booking_trucks(self,):
        self.list_all
        mini_list = []
        ans = input("Вы хотите забронировать транспорт? ('да', 'нет') ")
        if ans == 'да':
            for i in self.list_all:
                if i[5] == False:
                    print(f'Тип: {i[0]}, грузоподъемность: {i[1]} т, длина: {i[2]} м, ширина: {i[3]} м, высота: {i[4]} м')
                    mini_list.append(i)
            ans = input("Введите какой хотите забронировать: ")
            for i in range(len(self.list_all)):
                if self.list_all[i][0] == ans:
                    print("Забронирован для вас")
                    # self.list_all[i][5] = True    Надо доработать бронь фур
                    
                    print(self.list_all)
    
    def booking_with_name(self, name):
        for i in range(len(self.list_all)):
            if self.list_all[i][0] == name:
                self.booking = True
                print("Забронирован для вас")
                

            
truck_1 = Trucks('Газель', '2', '3.1-3.9', '2', '1.7-2.2', True)
truck_2 = Trucks('Бычок', '3', '4.2-5', '2-2.2', '2-2.4', False)
truck_3 = Trucks('MAN-10', '10', '6-8', '2.45', '2.3-2.7', True)
truck_4 = Trucks('Фура', '20', '13.6', '2.46', '2.5-2.7', False)


list_all_trucks = []
list_all_trucks.append(truck_1)
list_all_trucks.append(truck_2)
list_all_trucks.append(truck_3)
list_all_trucks.append(truck_4)


def sortong():
    back = input("Отменить сортировку (да/нет) ")
    if back == 'нет':
        global sort_list
        parametr = input("По какому параметру сортировать ('тип', 'грузоподъемность', 'длина', 'ширина', 'высота', 'бронь'): ")
        if parametr not in ('тип', 'грузоподъемность', 'длина', 'ширина', 'высота', 'бронь'):
            print('Неправильный параметр ')
        order = input("По возрастанию ('да', 'нет'): ")
        if order not in ('да', 'нет'):
            print('Неправильный ввод ')
        truck_1.Sort(parametr, order)

def booking_truck(truck):
    # truck.booking_trucks()
    mini_list = []
    ans = input("Вы хотите забронировать транспорт? ('да', 'нет') ")
    if ans == 'да':
        truck.get_booking_info(False)
    ans = input("Введите какой хотите забронировать: ")
    if ans == 'Газель':
        truck_1.booking_with_name(ans)
    elif ans == 'Бычок':
        truck_2.booking_with_name(ans)
    elif ans == 'MAN-10':
        truck_3.booking_with_name(ans)
    elif ans == 'Фура':
        truck_4.booking_with_name(ans)
    
    



def get_weigth():
    key = False
    while key == False:
        weigth = float(input("Какой грузоподъемности вам нужен транспорт, веддите число Тонн: "))
        if weigth.is_integer():
            a = truck_1.get_weight_info(weigth)
            print(a)
            key = True
        else:
            print("Вы вели некорректные данные ")


# list(map(float, a.split("-")))  вывод в флоат длины ширины высоты

# print(truck_1.get_all())

while True:
    command = input('Выберите команды: сортировать = 1, узнать свободные = 2, грузоподъемность = 3, узнать занятые = 4, забронировать транспорт = 5, выйти ')
    if command == '1':
        sortong()
    elif command == '2':
        print(truck_1.get_booking_info(False))
    elif command == '3':
        get_weigth()
    elif command == 'выйти':
        break
    elif command == '4':
        print(truck_1.get_booking_info(True))
    elif command == '5':
        booking_truck(truck_1)
    else:
        print('Неверная команда')


# Надо сделать красивый вывод 

alll = (['Газель', '2', '3.1-3.9', '2', '1.7-2.2', True],
 ['Бычок', '3', '4.2-5', '2-2.2', '2-2.4', False],
[']MAN-10', '10', '6-8', '2.45', '2.3-2.7', True],
['Фура', '20', '13.6', '2.46', '2.5-2.7', False])

print(alll)
print(123)
sqlite.sql(alll)  # сгружать все в бд