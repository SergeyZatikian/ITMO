"""
N рублей сдача
M_1 монет номиналом S_1
M_2 монет номиналом S_2
M_3 монет номиналом S_3
Наименьшую кобминацию
"""
def GetInfo():
    global N
    N = int(input("Введите количесвто монет "))
    global coins
    coins = dict()
    for i in range(N):
        value = int(input("Введите номинал монеты  "))
        coins[value] = int(input("Введите количечство монет с этим номиналом "))

def PrintInfo():
    for i in coins.keys():
        print(f"{coins.get(i)} монет номиналом {i}")

def list_of_all(coins = dict()):
    list_coin = list()
    for i in coins.items():
        list_coin += (str(i[0])*i[1])
    return(list(map(int, list_coin)))

coins = {5: 10, 2: 20, 1: 25}
N = 114

#PrintInfo()
cnt, S = 0, 0
#print(list_of_all(coins), sum(list_of_all(coins)))
lst = list()

for i in list_of_all(coins):
    if S != N and S <= N and S+i <= N:
        lst.append(i)
        cnt += 1
        S += i

if S < N:
    print("Количество монет не хвататет для сдачи")

print(f"Минимальное количесвто монет в сдаче {cnt}")
#print(N, cnt, S, lst)
