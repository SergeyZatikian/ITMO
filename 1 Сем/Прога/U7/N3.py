def dif(p):
    cnt = 0
    if len(p) != 0: cnt += 1
    if len(p) >= 8: cnt += 1
    k_0, k_1, k_2, k_3 = False, 0, 0, 0
    for i in p:
        if i.isdigit():
            k_0 = True
        if i.islower():k_1 = 1
        if i.istitle():k_2 = 1
        if i in  ".,:;!_*-+()/#¤%&)": k_3 = True
    if k_0: cnt += 1
    if k_1 + k_2 == 2: cnt += 1
    if k_3: cnt += 1
    return cnt
password = input('Введите пароль ')
print('Сложность данного пароля ', dif(password))