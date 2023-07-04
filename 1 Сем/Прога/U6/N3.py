def length(v1, t1):
    return v1*t1

print("Введите V1:")
v1 = float(input())
print("Введите V2:")
v2 = float(input())
print("Введите t1:")
t1 = float(input())
print("Введите t2:")
t2 = float(input())
print(length(v1, t1) + length(v2, t2))