class Triangle:
    def geron(self, a, b, c):
        p = (a+b+c)//2
        #S = (p*(p-a)*(p-b)*(p-c))*0.5
        print((p*(p-a)*(p-b)*(p-c))**0.5)


prog = Triangle()
a = int(input('Введите первую сторону треугольника: '))
b = int(input('Введите вторцю сторону треугольника: '))
c = int(input('Введите третью сторону треугольника: '))
if a == 0 or b == 0 or c == 0 or a+b<c or a+c<b or c+b<a:
    print('Такого треугольника не существует')
else:
    prog.geron(a, b, c)