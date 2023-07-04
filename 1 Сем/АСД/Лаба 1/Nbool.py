from re import L


print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not x and y) or (x and z) :
                print(x, y, z, 1)
            else:
                print(x, y, z, 0)