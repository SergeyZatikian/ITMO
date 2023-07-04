from random import randint
from abc import abstractmethod

@abstractmethod
class Fighter():

    def __init__(self, name = "Боец"):
        self.name = name
        self.__start_health()
        self.damage = 20

    def get_name(self): #возвращаем имя
        return self.name
    
    def give_health(self): #возвращаем хп
        return self.health
    
    def __add__(self, new_name): #перегрузка сложение
        return self.name + new_name

    def is_alive(funct): #декоратор
        def live(self):
            if  self.health <= 0:
                return False
            else: 
                return True
        return live

    @is_alive
    def live(self): #проверка на жив ли или нет
        if  self.health <= 0:
            return False
        else: 
            return True

    def __start_health(self): #инкаспуляцияя начальное хп
        self.health = 100  
    
    @abstractmethod
    def print_info(self): #абстрактный метод вывод информации о бойце
        print("Тут в будущем будет вся инфа о бойце и его способностях")

    def one_step(self, enemy_damage): #шаг(удар, действие)
        self.health -= enemy_damage

    def give_damage(self): #вывод урона
        return self.damage

class Wrestling(Fighter): #борец
    
    def __init__(self, name):
        Fighter.__init__(self, name)
        self.health = 120

class Jiu_jitsu(Fighter): #Владеет Джиу Джитсу
    pass

class Boxing(Fighter): #Боксер
    
    def __init__(self, name):
        Fighter.__init__(self, name)


    def print_info(self):
        print("Ваш боец боксер")
        return super().print_info()

    def give_damage(self): #Повышенный урон с вероятностью 20%
        if randint(1,5) == 1:
            return self.damage + 10
        else:
            return self.damage

class Boss(Boxing, Jiu_jitsu, Wrestling): #класс босс повышенный урон и хп
    def __init__(self, name):
        Boxing.__init__(self, name)
        Jiu_jitsu.__init__(self, name)
        Wrestling.__init__(self, name)
        self.name = name
        self.health = 500
        self.damage = 100
    
    def get_name(self):
        return self.name

class God(Boss): #класс бог урон ниже чем у босса, но хп больше 

    def __init__(self, name):
        Boss.__init__(self, name)
        self.health = 700
        self.damage = 80
        self.name = name

    def get_name(self):
        return self.name
