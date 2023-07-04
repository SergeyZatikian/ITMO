class Doctor:
    def __init__(self, name='Айболит', age=25):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name


class Pediatrist(Doctor):
    def __init__(self):
        super().__init__()
        self.specialization = 'Pediatrist'

    def getName(self):
        return self.name, self.specialization


class Oculist(Doctor):
    def __init__(self):
        super().__init__()
        self.specialization = 'Oculist'

    def getName(self):
        return self.name, self.specialization


class Dentist(Doctor):
    def __init__(self):
        super().__init__()
        self.specialization = 'Dentist'

    def getName(self):
        return self.name, self.specialization


d1 = Pediatrist()
d2 = Oculist()
d3 = Dentist()

d3.setName('Маша')
d1.setName('Илья')
d2.age = 20
d3.age = 35

print(*d1.getName(), d1.age)
print(*d2.getName(), d2.age)
print(*d3.getName(), d3.age)

