import math 
def disr(a, b, c):
    D = b**2 - 4*a*c
    x_1 = (-b + D**0.5)/2*a
    x_2 = (-b - D**0.5)/2*a
    if D < 0:
        print('У уравнение нет корней')
    if D == 0 and x_1 == x_2:
        print('Уравнение имеет один корень ',x_1)
    else:
        print('Уравнение имеет два корня ', x_1, x_2)

a, b, c = map(float, input("Введит коэфиценты квадратного уравнения(a*x^2 + b*x + c): ").split())
print(disr(a, b, c))
