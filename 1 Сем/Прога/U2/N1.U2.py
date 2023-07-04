a = input("Введите имя ")
b = input("Введите пол М/Ж ")
c = int(input("Введите возраст "))

if b == "М" or b == "м":
    if c%10 in [2, 3, 4] and c%100 not in [11, 12, 13, 14]:
        print("Его зовут " + a + ". Ему " + str(c) + " года.")
    elif c%10 in [1] and c%100 not in [11, 12, 13, 14]:
        print("Его зовут " + a + ". Ему " + str(c) + " год.")
    elif c%10>4 or c%100 in [11, 12, 13, 14]:
        print("Его зовут " + a + ". Ему " + str(c)+" лет.")
else:
    if c%10 in [2, 3, 4] and c%100 not in [11, 12, 13, 14]:
        print("Ее зовут " + a + ". Ей " + str(c) + " года.")
    elif c%10 in [1] and c%100 not in [11, 12, 13, 14]:
        print("Ее зовут " + a + ". Ей " + str(c) + " год.")
    elif c%10>4 or c%100 in [11, 12, 13, 14]:
        print("Ее зовут " + a + ". Ей " + str(c) + " лет.")
