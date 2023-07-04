graph = {}

n = int(input('Введите количество строк: '))
matrix = []
for i in range(n):
    a = input('Введите строку: ')
    matrix.append(list(map(int, a.split())))

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            graph[str((i, j))] = []
            new_i_back = i - 1
            new_i_forward = i + 1
            new_j_back = j - 1
            new_j_forward = j + 1
            if (new_i_back >= 0) and (matrix[new_i_back][j] == 0):
                graph[str((i, j))].append(str((new_i_back, j)))
            if (new_i_forward <= n - 1) and (matrix[new_i_forward][j] == 0):
                graph[str((i, j))].append(str((new_i_forward, j)))
            if (new_j_back >= 0) and (matrix[i][new_j_back] == 0):
                graph[str((i, j))].append(str((i, new_j_back)))
            if (new_j_forward <= n - 1) and (matrix[i][new_j_forward] == 0):
                graph[str((i, j))].append(str((i, new_j_forward)))
for i in graph:
    print(i, graph[i])


start_i = int(input("Введите номер строки: "))
start_j = int(input("Введите номер столбца: "))


visited = set()
path = []
flag = False
def DFS(n):
    global flag
    if (not(flag)):
        if n in visited:
            return
        visited.add(n)
        path.append(n)
        for i in graph[n]:
            if not i in visited:
                DFS(i)
        if int(n[n.index(' ') + 1:len(n) - 1]) == len(matrix) - 1:
            flag = True
        if not(flag):
            path.pop()

DFS(str((start_i, start_j)))

'''
if (flag):
    print(path)
else:
    print("Выхода нет")
'''

if (flag):
    for i in range(n):
        for j in range(n):
            if not (str((i, j)) in path):
                print("*", end=" ")
            else:
                print("8", end=" ")
        print()
else:
    print("Выхода нет")
