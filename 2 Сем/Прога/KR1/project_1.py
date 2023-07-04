import random

class Fighter():

    def __init__(self, name,  health = 100) -> None:
        self.health = health
        self.name = name

    def get_name(self):
        #print(self.name)
        return self.name
    
    def get_health(self):
        return self.health

    def get_newhealth(self, new_health):
        self.health = new_health
        return new_health
        #print(new_health)

class Wrestling(Fighter):
    pass

class Jiu_jitsu(Fighter):
    pass

class Boxing(Fighter):
    pass

def getInfo():
    name_1 = input("Выбери имя первого бойца: ")
    style_1 = input("Выбери стиль первого бойца (борьба = 1, бокс = 2, джиу джитсу = 3): ")
    name_2 = input("Выбери имя второго бойца: ")
    style_2 = input("Выбери стиль второго бойца (борьба = 1, бокс = 2, джиу джитсу = 3): ")
    global person_1
    global person_2
    if style_1 == "1" or style_1 == "борьба" :
        person_1 = Wrestling(name_1)
    elif style_1 == "2" or style_1 == "бокс":
        person_1 = Boxing(name_1)
    elif style_1 == "3" or style_1 == "джиу джитсу":
        person_1 = Jiu_jitsu(name_1)

    if style_2 == "1" or style_2 == "борьба" :
        person_2 = Wrestling(name_2)
    elif style_2 == "2" or style_2 == "бокс" :
        person_2 = Boxing(name_2)
    elif style_2 == "3" or style_2 == "джиу джитсу" :
        person_2 = Jiu_jitsu(name_2)

getInfo()

def fight(person_1, person_2, h_1, h_2):
    step = random.randint(0, 1)

    if person_1.get_health() == 0:
        print(f"Победил(a) боец {person_2.get_name()}")
        exit
    elif person_2.get_health() == 0:
        print(f"Победил(a) боец {person_1.get_name()}")
        exit

    else:
        if step == 0:
            h_2 -= 20
            print(f"Боец {person_1.get_name()} ударил(a) {person_2.get_name()}. У {person_2.get_name()} осталось {person_2.get_newhealth(h_2)} здоровья")
            return (fight(person_1, person_2, h_1, h_2))
        if step == 1:
            h_1 -= 20
            print(f"Боец {person_2.get_name()} ударил(a) {person_1.get_name()}. У {person_1.get_name()} осталось {person_1.get_newhealth(h_1)} здоровья")
            return (fight(person_1, person_2, h_1, h_2))
        
fight(person_1, person_2, person_1.get_health(), person_2.get_health())
