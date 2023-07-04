class Country:
    def __init__(self, capital='None', population=100):
        self.capital = capital
        if population <= 0:
            print("Отрицательное население")
            self.population = 0
        else:
            self.population = population

    def setPopulation(self, new_population):
        self.population = new_population

    def getPopulation(self):
        return self.population


class Russia(Country):
    def __init__(self):
        super().__init__()
        self.capital = 'Moscow'


class Germany(Country):
    def __init__(self):
        super().__init__()
        self.capital = 'Berlin'


class Canada(Country):
    def __init__(self):
        super().__init__()
        self.capital = 'Ottawa'


c1 = Russia()
c2 = Canada()
c3 = Germany()

c1.setPopulation(146000000)
c2.setPopulation(38250000)
c3.setPopulation(83200000)

print(c1.capital, c1.getPopulation())
print(c2.capital, c2.getPopulation())
print(c3.capital, c3.getPopulation())