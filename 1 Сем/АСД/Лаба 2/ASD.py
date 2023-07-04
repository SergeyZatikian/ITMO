matrix = [[1,2,3], [4, 5, 6]]

new_matrix = list()

for i in range(len(matrix)):
    print(matrix[i])

trans_matrix = list()
for a in range(len(matrix[0])):
    lis = list()
    for b in matrix:
        lis.append(b[a])
    trans_matrix.append(lis)

for i in range(len(trans_matrix)):
    print(trans_matrix[i])
print(3 + len(matrix[0])*2 + len(matrix[0])*len(matrix))
