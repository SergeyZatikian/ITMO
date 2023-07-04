class Soda:
    def show_my_drink(self, a):
        if len(a) != 0:
            print('Кофе ' + a)
        else:
            print('Черный кофе')

soda = Soda()
soda.show_my_drink(str(input('Введите наименование добавки, если оно есть: ')))