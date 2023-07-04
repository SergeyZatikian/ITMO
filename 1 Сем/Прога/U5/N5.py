login = set()
login.add('sergey')
login.add('roma')
login.add('masha')
login.add('ivanov')
login.add('pupkin')
login.add('emir')
login.add('damir')
login.add('rustam')

log = input("Введите логин: ")
if (log in login):
    print("Разрешить доступ")
else:
    print("Доступ запрещен. Желаете добавить свой логин?")
    answer = input()
    if (answer == 'да') or (answer == 'Да'):
        login.add(log)
        print("Логие добавлен. Доступ разрешен")
        print(login)
    elif (answer == 'нет') or (answer == 'Нет'):
        print("Логин не добавлен, доступ запрещен")