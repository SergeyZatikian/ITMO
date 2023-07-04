from math import pi

def krug(radius): #Функция по поиску площади круга
    sq_cir = pi*radius*radius
    return sq_cir

def pramougolnik(a, b): #Функция по поиску площади прямоугольника
    sq_rect = a*b
    return sq_rect

def treugolnik(a, b, c): #Функция по поиску площади треугольника
    p = (a+b+c)/2
    sq_triag = (p*(p-a)*(p-b)*(p-c))**0.5
    return sq_triag

while True:
    fun = input("Введите 1, чтобы найти площадь круга.\nВведите 2, чтобы найти площадь прямоугольника.\nВведите 3, чтобы найти площадь треугольника.\nВведите Q, чтобы выйти из программы.\n")

    try:
        match fun:
            case '1':
                rad = float(input("Введите радиус круга: "))
                if rad >= 0:
                    print(krug(rad))
                else:
                    raise ValueError
            case '2':
                a_, b_ = map(float, input("Введите тве стороны прямоугольника: ").split())
                if a_ > 0 and b_ > 0:
                    print(pramougolnik(a_, b_))
                else:
                    raise ValueError
            case '3':
                a_, b_, c_ = map(float, input("Введите три стороны треугольника: ").split())
                if (a_ > 0 and b_ > 0 and c_ > 0) and (a_+b_>c_ and c_+b_>a_ and a_+c_>b_):
                    print(treugolnik(a_, b_, c_))
                else:
                    raise ValueError
            case 'Q':
                break
            case _:
                print("Такой команды не существует.")
    except ValueError:
        print("Введите числа с плавающей запятой и положительные.")

    print('\n')