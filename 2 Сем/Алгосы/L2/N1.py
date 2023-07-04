#Метод деления
print(ord('1')) #в юникод
print(hex(49))  #в 16 строку
print(bin(10))  #в двоичный 
s = input('Ввод строки: ') 
news = []
for i in s:
    news += [ord(i)] #ввод в массив номера из таблицы Юникод
#print(news)
key = ord('я') + 1
for i in range(len(news)):
    news[i] = hex(key % news[i])[2:].zfill(2)
print(' '.join(news))
