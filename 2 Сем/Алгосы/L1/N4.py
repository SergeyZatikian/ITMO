import datetime
a, b = ('2023-02-07').split('-'), input('Введите: год-месяц-день: ').split('-')
aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
print(str((aa-bb)).split()[0])