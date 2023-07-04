import random
from FightBibl import Boxing

p = Boxing('Pasha')

print(p.get_name())
print(p.give_health())  #выдает здоровье
print(p.live())         #проверяет жив ли я
p.one_step(20)          #делает один удар
print(p.give_health())  #выдает здоровье
print(p.give_damage())  #выводит урон
p.one_step(p.give_damage())
print(f"У {p.get_name()} осталось { p.give_health()} здоровья")