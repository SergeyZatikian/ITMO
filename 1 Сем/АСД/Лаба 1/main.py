F = open('asdasd.txt', 'r', encoding='utf-8')
all_students = []
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
    all_students.append(student)
print(all_students)