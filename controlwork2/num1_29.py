'''В матрице F размером 5 х 7 удалить столбец, расположенный после столбца,
 содержащего минимальный по модулю элемент во 2-й строке.'''


#create 5*7 matrix
matrix = [
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 2, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34, 35]
]


indx_min_elem=0
min_elem = matrix[1][0]
for i in range(1, 7):
    if abs(matrix[1][i])<min_elem: 
        min_elem = abs(matrix[1][i])
        indx_min_elem = i
print(indx_min_elem)
new_matrix = [0 for _ in range(5)]
for i in range(5):
    row = []
    for j in range(7):
        if j!=indx_min_elem+1:
            row.append(matrix[i][j])
    new_matrix[i] = row

#matrix = [matrix[0][:indx_min_elem] + matrix[0][indx_min_elem+1:]] + matrix[1:]

for i in new_matrix:
    print(i)
#print(matrix)
