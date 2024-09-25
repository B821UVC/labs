'''В матрице В размером 6 × 6 поменять местами максимальные
элементы 1-й и 2-й строк, 3-й и 4-й, 5-й и 6-й.'''

matrix_B = [
    [3,19,-75,42,-26, -34],
    [85, 7, -61, 50, -28, 30],
    [-70, 26, -20, 38, -8, 11],
    [0, 15, 0, 999, -45, 17],
    [-63, 44, 71, -31, 22, 4],
    [56, 313, -78, -12, 55, 23],
]
mx_num_ps = [-10**20 for x in range(12)]  #values and positions
for st in range(6):
    for col in range(6):
        if mx_num_ps[2*st]<matrix_B[st][col]:
            mx_num_ps[2*st]=matrix_B[st][col]
            mx_num_ps[1+2*st]=col

matrix_B[0][mx_num_ps[1]], matrix_B[1][mx_num_ps[3]] = mx_num_ps[2], mx_num_ps[0]  #all +4 in mx_num_ps
matrix_B[2][mx_num_ps[5]], matrix_B[3][mx_num_ps[7]] = mx_num_ps[6], mx_num_ps[4]
matrix_B[4][mx_num_ps[9]], matrix_B[5][mx_num_ps[11]] = mx_num_ps[10], mx_num_ps[8]   
#ужасно

for str in matrix_B:  
    print(str)

