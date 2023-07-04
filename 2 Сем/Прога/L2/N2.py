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

c1, c2, c3 = Russia(), Canada(), Germany()

c1.setPopulation(143000000)
c2.setPopulation(38250000)
c3.setPopulation(83200000)

print(type(c1).__name__, c1.capital, c1.getPopulation())
print(type(c2).__name__, c2.capital, c2.getPopulation())
print(type(c3).__name__, c3.capital, c3.getPopulation())
