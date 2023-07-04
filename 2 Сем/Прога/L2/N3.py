class Games:
    def __init__(self, name='GTA5', year=2015):
        self.name = name
        self.year = year
    def getName(self):
        return self.name
    def setName(self, new_name):
        self.name = new_name

class PCGames(Games):
    def __init__(self):
        super().__init__()
        self.tech = 'PC'
    def getName(self):
        return self.name, self.tech


class PS4Games(Games):
    def __init__(self):
        super().__init__()
        self.tech = 'PS4'
    def getName(self):
        return self.name, self.tech


class XboxGames(Games):
    def __init__(self):
        super().__init__()
        self.tech = 'Xbox'
    def getName(self):
        return self.name, self.tech

class MobileGames(Games):
    def __init__(self):
        super().__init__()
        self.tech = 'Mobile'
    def getName(self):
        return self.name, self.tech

d1 = PCGames()
d2 = PS4Games()
d3 = XboxGames()
d4 = MobileGames()

d3.setName('Forza 4')
d1.setName('Mortal Kombat XL')
d4.setName('PUBG Mobile')
d2.year = 2013
d3.year = 2018
d4.year = 2019

print(*d1.getName(), d1.year)
print(*d2.getName(), d2.year)
print(*d3.getName(), d3.year)
print(*d4.getName(), d4.year)

