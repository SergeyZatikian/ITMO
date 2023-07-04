class Cat:
    def __init__(self, name, age):
        self.name = name
        if age > 19:
            self.age = 19
        elif age <= 0:
            self.age = 1
        else:
            self.age = age


class Sphinx(Cat):
    hair = 'лысый'
    action = 'охотник'


class MaineCoon(Cat):
    hair = 'длинная'
    action = 'крысолов'


class Corat(Cat):
    hair = 'средняя'
    action = 'играет'


cat1 = Sphinx('рыжик', 4)
cat2 = MaineCoon('уголёк', 20)
cat3 = Corat('Бегемот', -5)

print(cat1.name, cat1.age, cat1.hair, cat1.action)
print(cat2.name, cat2.age, cat2.hair, cat2.action)
print(cat3.name, cat3.age, cat3.hair, cat3.action)
