class Dog:
    def __init__(self, name, age):
        self.name = name
        if age > 19:
            self.age = 19
        elif age <= 0:
            self.age = 1
        else:
            self.age = age


class ToyTeyrer(Dog):
    voice = 'писклявый'
    action = 'домашняя'


class Spaniel(Dog):
    voice = 'грациозный'
    action = 'охотничья'


class NemeckayOvcharka(Dog):
    voice = 'грозный'
    action = 'сторожевая'


dog1 = ToyTeyrer('Боб', 4)
dog2 = Spaniel('Шарик', 20)
dog3 = NemeckayOvcharka('Ибрагим', -5)

print(dog1.name, dog1.age, dog1.voice, dog1.action)
print(dog2.name, dog2.age, dog2.voice, dog2.action)
print(dog3.name, dog3.age, dog3.voice, dog3.action)
