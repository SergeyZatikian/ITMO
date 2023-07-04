def xor_cipher( str, key ):
    encript_str = ""
    for letter in str:
        encript_str += chr( ord(letter) ^ key )
    return  encript_str  

stroka = input("Введите строку, которую хотите зашифровать: ")
key = input("Введите ключ шифра: ")
print(xor_cipher(stroka, key))
