import random
from FightBibl import Fighter, Boxing, Jiu_jitsu, Wrestling, God, Boss
from errors import *
import threading
import sqlite3

def getInfo():
    while True:
        name_1 = input("Выбери имя первого бойца: ")
        style_1 = (input("Выбери стиль первого бойца (борьба = 1, бокс = 2, джиу джитсу = 3): "))
        name_2 = input("Выбери имя второго бойца: ")
        style_2 = (input("Выбери стиль второго бойца (борьба = 1, бокс = 2, джиу джитсу = 3): "))
            
        # if style_1 not in "1" or style_1 not in "2" or style_1 not in "3"  and style_2 not in "1" or style_2 not in "2" or style_2 not in "3":
        #     raise Error()
        
        global person_1
        global person_2

        if style_1 == "1" or style_1 == "борьба" :
            person_1 = Wrestling(name_1)
        elif style_1 == "2" or style_1 == "бокс":
            person_1 = Boxing(name_1)
        elif style_1 == "3" or style_1 == "джиу джитсу":
            person_1 = Jiu_jitsu(name_1)
        else: print('Неверный ввод')

        if style_2 == "1" or style_2 == "борьба" :
            person_2 = Wrestling(name_2)
            break
        elif style_2 == "2" or style_2 == "бокс" :
            person_2 = Boxing(name_2)
            break
        elif style_2 == "3" or style_2 == "джиу джитсу" :
            person_2 = Jiu_jitsu(name_2)
            break
        else: print('Неверный ввод')

def vibor(style_1, style_2, name_1, name_2):
    global person_1
    global person_2

    if style_1 == "1" or style_1 == "борьба" :
        person_1 = Wrestling(name_1)
    elif style_1 == "2" or style_1 == "бокс":
        person_1 = Boxing(name_1)
    elif style_1 == "3" or style_1 == "джиу джитсу":
        person_1 = Jiu_jitsu(name_1)
    else: print('Неверный ввод')

    if style_2 == "1" or style_2 == "борьба" :
        person_2 = Wrestling(name_2)
        
    elif style_2 == "2" or style_2 == "бокс" :
        person_2 = Boxing(name_2)
        
    elif style_2 == "3" or style_2 == "джиу джитсу" :
        person_2 = Jiu_jitsu(name_2)
        

text = []
#getInfo()
def fight(person_1, person_2):

    if person_2.live() and person_1.live():
        if random.randint(0, 1) == 0:
            person_2.one_step(person_2.give_damage())
            if person_2.live():
                
                print(f"Боец {person_1.get_name()} ударил(a) бойца {person_2.get_name()}. У {person_2.get_name()} осталось {person_2.give_health()} здоровья\n")
                text.append(f"Боец {person_1.get_name()} ударил(a) бойца {person_2.get_name()}. У {person_2.get_name()} осталось {person_2.give_health()} здоровья\n")
            else:
                print(f"Боец {person_1.get_name()} ударил(a) бойца {person_2.get_name()}. Победил(a) боец {person_1.get_name()}\n")
                text.append(f"Боец {person_1.get_name()} ударил(a) бойца {person_2.get_name()}. Победил(a) боец {person_1.get_name()}")
            return (fight(person_1, person_2))
        else:
            person_1.one_step(person_1.give_damage())
            if person_1.live():
                print(f"Боец {person_2.get_name()} ударил(a) бойца {person_1.get_name()}. У {person_1.get_name()} осталось {person_1.give_health()} здоровья\n")
                text.append(f"Боец {person_2.get_name()} ударил(a) бойца {person_1.get_name()}. У {person_1.get_name()} осталось {person_1.give_health()} здоровья\n")
            else:
                print(f"Боец {person_2.get_name()} ударил(a) бойца {person_1.get_name()}. Победил(a) боец {person_2.get_name()}\n")
                text.append(f"Боец {person_2.get_name()} ударил(a) бойца {person_1.get_name()}. Победил(a) боец {person_2.get_name()}")
            return (fight(person_1, person_2))

person_1 = Boxing('Глеб')
person_2 = Wrestling('Маша')
# person_3 = God('Аиша')
# person_4 = Boss('Вахтанг')

fight_1 = threading.Thread(target=fight, args=(person_1, person_2,))
# fight_2 = threading.Thread(target=fight, args=(person_3, person_4,))
fight(person_1, person_2)
print()
# fight(person_3, person_4)

# con = sqlite3.connect('Persons.db') #создать курсор для выполнения запросов
# cur = con.cursor()

# con.execute("""
#     CREATE TABLE IF NOT EXISTS Persons (
#         count INTEGER PRIMARY KEY ,
#         names VARCHAR(30)
# );           
#     """)

# data = [(1, person_1.get_name()), (2, person_2.get_name()), (3, person_3.get_name()), (4,person_4.get_name())]
# cur.execute("INSERT INTO Persons (count, names) VALUES (6, 'Иван')")
# cur.execute('SELECT * from Persons')
# row = cur.fetchall()
# print(row)

# if(con):
#     con.commit()
#     con.close()
#     print("Все сделано БОСС")

for i in text:
    print(i)