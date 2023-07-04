F = open("C:\\Users\\36050\\OneDrive\\Рабочий стол\\1 сем\\АСД\\Лаба 2\\Aki.txt", 'r', encoding='utf-8')
all_students = []
for i in F:
    ind = 0
    student_info = i.split()[-23:]
            # Имя    Д?     18?    Очки?  Карие? Брюнет? 
    student = {0:'', 1: '', 2: '', 3: '', 4: '', 5: '',
            #  Брат\сестр   Дом жив     Из спб      Айфон       У Тушавина      Кофе    Дом еда
               6: '',       7: '',      8: '',      9: '',      10: '',         11: '', 12: '',
            #  Часы?   Имя с глас   Пицца?  Курите?   Выше 175  Половинка?  Родились зимой?  Играете долго в доту или кс
               13: '', 14: '',      15: '', 16: '',   17: '',   18: '',     19: '',          20: '',
            #  Общага  Фильмы  Аниме
               21: '', 22: '', 23: ''}
    for key in list(student.keys())[1:]:
        student[key] = student_info[ind].lower()
        ind += 1
    student[0] = i.split()[0]
    all_students.append(student)
        
'''
for i in all_students:
    print(i)
'''

print('Везде ответы либо да, либо нет')
Gender = str(input('Ты девушка? '))
Age = str(input('Тебе 18? '))
Glass = str(input('Вы носите очки? '))
Eye_color = str(input('У тебя карие глаза? '))
Hair_color = str(input('У тебя темные волосы? '))
Sibl = str(input('У тебя есть братья или сестры? ' ))
Pets = str(input('У тебя есть домашние животные? '))
From_spb = str(input('Ты из СПБ? '))
Iphone = str(input('У тебя айфон? '))
Linal = str(input('Ты учишься у Тушавина? '))
Cofee = str(input('Ты любишт больше кофе чем чай? '))
Food = str(input('Тебе нравиться больше домашняя еда чем уличная? '))
Watch = str(input('Ты носишь часы? '))
Name = str(input('Твое имя начинается с гласной? '))
Pizza = str(input('Тебе нравится больше пицца чем суши? '))
Smoke = str(input('Ты куришь? '))
High = str(input('Твой рост больше 175? '))
Half = str(input('У тебя есть вторая половинка? '))
if Gender == 'нет':
    Winter = str(input('Ты родился зимой? '))
else:
    Winter = str(input('Ты родилась зимой? '))
Game = str(input('Ты играешь в кс или доту больше 100 часов? '))
Hostel = str(input('Ты живешь в общаге? '))
Kino = str(input('Ты больше любишь кино чем сериалы? '))
Anime = str(input('Ты смотришь аниме? '))

questions = ( Gender, Age, Glass, Eye_color, Hair_color, Sibl, Pets, From_spb, Iphone, Linal, Cofee, Food, Watch, Name, Pizza, Smoke, High, Half, Winter, Game, Hostel, Kino, Anime)
#print(all_students[4])
#print(questions)
for i in all_students :
    k = True
    for a in range(len(questions)):
        #print(a, i[a], questions[a])
        if i[a+1] != questions[a]:
            k = False
            #print(i[0])
            break
    if k:
        print (i[0])
