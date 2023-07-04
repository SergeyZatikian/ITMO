matrix = [[1,1,1], [1, 1, 1]]

new_matrix = list()

for i in range(len(matrix)):
    print(matrix[i])

def transposition(matrix):
    trans_matrix = list()
    for a in range(len(matrix[0])):
        lis = list()
        for b in matrix:
            lis.append(b[a])
        trans_matrix.append(lis)
    return(trans_matrix)
for i in range(len(transposition(matrix))):
    print(transposition(matrix)[i])

mat1 = [[3, 4],[5, 1]]
mat2 = [[8, 1],[2, 3]]
def matrix_multiplication(mat1, mat2):
    if len(mat1[0]) == len(mat2):
        result = [[0 for i in range(len(mat2[0]))] for j in range(len(mat1))]
        for i in range(len(result[0])):
            for j in range(len(result)):
                result[i][j] = sum(mat1[i][n] * mat2[n][j] for n in range(len(mat2)))
        return result
    else:
        return 'Error'
print()
for i in range(len(matrix_multiplication(mat1, mat2))):
    print((matrix_multiplication(mat1, mat2))[i])
print()
def matrix_rang (matrix):
    matrix_copy = matrix.copy ()
    for a in matrix_copy:
        if a == [0] * len (a):
            matrix.remove (a) # тут мы убираем нулевые строки
    for b in range (len (matrix)):   # b индекс строки
        dell = 1 # число на которое делим 
        for d in range (len (matrix [b])): # Ищем первое ненулевое значение
            if matrix [b][d] != 0: 
                dell = matrix [b][d] # первое ненулевое значение
                break
        if [0] * len (matrix [b]) != matrix [b]: # строка не состоит из нулей
            matrix [b] = [matrix [b][i] / dell for i in range (len (matrix [b]))]
            # делим элементы строки на первый не нулевой элемент
            for j in range (b + 1, len (matrix)): 
                k = matrix [j][d] / matrix [b][d] 
            #  для каждой следующей находим отношение элемента b строки 
            # с индексом d и элемента b строки с индексом d
                matrix [j] = [matrix [j][i] - k * matrix [b][i] for i in range (len (matrix [j]))] 
                # для каждого элемента строки j мы вычитаем из него соответствующий ему элемент строки j, умноженный на k 
    rank_matrix = len(matrix)
    for i in matrix: # при нулевой строке -1 из ранга 
        O = True
        for el in i:
            if el != 0:
                O = False
                break
        if O:
            rank_matrix -= 1
    return rank_matrix
print("rang =",matrix_rang(matrix))
        