class Pupil:
    def __init__(self, name='Radomir', age=8, classNumber='1-A'):
        self.name = name
        self.age = age
        self.classNumber = classNumber

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    def set_classNumber(self, new_classNumber):
        self.classNumber = new_classNumber

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

    def get_classNumber(self):
        print(self.classNumber)

    def get_all(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)
        print("Номер класса:", self.classNumber)
        print()


p1 = Pupil()
p2 = Pupil()
p3 = Pupil()

p1.set_name("Petr")
p1.set_classNumber("2-A")

p2.set_name("Anna")
p2.set_age(12)

p3.set_age(11)
p3.set_classNumber("1-B")

p1.get_all()
p2.get_all()
p3.get_all()