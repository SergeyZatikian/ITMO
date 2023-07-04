F = open("C:\\Users\\36050\\OneDrive\\Рабочий стол\\АСД\\Aki.txt", 'r', encoding='utf-8')
database = []
for i in F:
    ind = 0
    student_info = i.split()[-23:]
    student = {'name': ' '.join(i.split()[2:-23]), 'Male': '', 'is_18': '', 'Glasses': '', 'Eyes': '', 'Hair': '',
            'Siblings': '', 'Pets': '', 'from_Peter': '', 'Iphone': '', 'Tushavin': '', 'Coffee': '', 'Food': '',
            'Watches': '', 'Name_Ending': '', 'Pizza': '', 'Smoke': '', 'Height': '', 'Love': '', 'Winter_born': '',
            'Games': '', 'Obshaga': '', 'Films': '', 'Anime': ''}
    for key in list(student.keys())[1:]:
        if student_info[ind] == 'Да':
            student[key] = True
        else:
            student[key] = False
        ind += 1
    database.append(student)

def take_chanсe(answer,property):
    if answer == 'y':
        ans=True
    else:
        ans=False

    to_remove=[]
    for i in database:
        if i[property] != ans:
            to_remove.append(i)
    for i in to_remove:
        database.remove(i)


    
q=[
    ['твой персонаж девушка?','Male'],
    ['твоему персонажу есть 18?','is_18'],
    ['твой персонаж носит очки?','Glasses'],
    ['у твоего персонажа карие глаза?','Eyes'],
    ['У твоего персонжа темные волосы?','Hair'],
    ['У него есть братья или сестры?','Siblings'],
    ['У него есть домашние животные?','Pets'],
    ['Он из Питера?','from_Peter'],
    ['У него есть Iphone?','Iphone'],
    ['У него практику по линалу ведет Тушавин?','Tushavin'],
    ['Он любит коффе больше чем чай?','Coffee'],
    ['Он предпочитает домашнию еду фастфуду?','Food'],
    ['Он носит часы?','Watches'],
    ['Его имя начинается с гласной буквы?','Name_Ending'],
    ['Он пиццу люит больше чем суши?','Pizza'],
    ['Он курит?','Smoke'],
    ['Его рост больше 175 см?','Height'],
    ['У него есть вторая половинка','Love'],
    ['Он родился в первой половине года?','Winter_born'],
    ['Он играет в копьютерные игры?','Games'],
    ['Он живет в общажитии?','Obshaga'],
    ['Фильмы он любит больше чем сериалы?','Films'],
    ['Он смотрит аниме?','Anime']
]    

for i in q:   
    ans=input(i[0])
    take_chanсe(ans,i[1])
    if len(database)==1:
        print('ты загадал '+database[0]['name'])
        break