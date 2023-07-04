a = input()
b = a.split()
a = float(b[0])
c = float(b[2])
b = b[1]
if b == "+":
    print(a+c)
if b == "-":
    print(a-c)
if b == "*":
    print(a*c)
if b == "/":
    if c != 0:
        print(a/c)
    else:
        print("На 0 делить нельзя")