def to_int(p):
    try:
        p = int(p)
    except:
        pass
    return p
 
def debit(obj):
    if type(obj) == int:
        return obj
    elif type(obj) == str:
        l = []
    for i in obj:
        l.append(ord(i))
    return l
  
def cipher(arg, key):
    if type(arg) == int and type(key) == int:
        return arg^key
    else:
        l_arg = debit(arg)
        l_key = debit(key)
    if type(l_key) == list:
        s_key = sum(l_key)
    else:
        s_key = l_key
    for i in range(len(l_arg)):
        l_arg[i] = chr(l_arg[i]^s_key)
  
    return ''.join(l_arg)

while True:
    message = input("Введите строку, которую хотите зашифровать: ")
    code = input("Введите ключ шифра: ")
    #if not code.isdigit():print("Ошибка, введите нормально ")
    message, code = to_int(message), to_int(code)
    print(cipher(message, code), '\n')