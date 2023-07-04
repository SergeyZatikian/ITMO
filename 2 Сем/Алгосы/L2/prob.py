def shift(x: int, s: int) -> int: # Функция для битового сдвига
    x = bin(x)[2:]
    print(x)
    x = x[s:] + x[:s]
    print(x)
    print(int(x,2))
    return int(x,2)

print(shift(85, 5))