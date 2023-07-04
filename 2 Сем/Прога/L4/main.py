class Math:
    def addition(self, a, b):
        print(a + b)
    def multiplication(self, a ,b):
        print(a * b)
    def division(self, a ,b):
        if b == 0:
            print('нельзя делить на 0')
        else:
            print(a / b)
    def subtraction(self, a, b):
        print(a - b)
try:
    dev = Math()
    a = int(input('Введите число a: '))
    b = int(input('Введите число b: '))
    ans = int(input('Введите 1 - для сложения, 2 - для умножения, 3 - для деления, 4 - для вычитания: '))
    if ans == 1:
        dev.addition(a, b)
    elif ans == 2:
        dev.multiplication(a, b)
    elif ans == 3:
        dev.division(a, b)
    elif ans == 4:
        dev.subtraction(a, b)
    else:
        print('Нет такого варианта ответа')
except:
    print('Что-то пошло не так')