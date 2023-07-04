def compl1(n):
    for i in range(n):
        print("Hello world!")
    for i in range(n):
        print("Hello world!")
    for i in range(n):
        print("Hello world!")

def compl2(n):
    return sorted(n)

def compl4(n):
    for i in range(n):
        for i in range(n):
            for i in range(n):
                print("How are you?")


a = [1, 3, 2, 5, 6, 8, 9, 123, 4, 5, 6]
compl1(2)
print(compl2(a))
compl4(2)