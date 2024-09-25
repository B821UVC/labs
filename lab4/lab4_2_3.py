'''Дана матрица А размером 10 × 5. Преобразовать матрицу следу-
ющим образом: заменить первый элемент столбца суммой элементов
столбца, расположенных после максимального элемента, если макси-
мальный элемент находится в первой половине столбца. В противном
случае оставить столбец без изменения.'''


import random
n=5 #cols
m=10
matrix_m_n = [[random.randint(-10, 10)for x in range(n)] for y in range(m)]

#matrix_m_n = [[10-x for x in range(n)] for y in range(m)]       #test
#matrix_m_n = [[x for x in range(n)] for y in range(m)]
for str in matrix_m_n:
    print(str)
for col in range(n):
    mx_val = -10**20
    ps_mx_val = 10**20
    sum_after_mx=0
    for str in range(m):
        val = matrix_m_n[str][col]
        if mx_val<val:
            mx_val = val
            ps_mx_val = str
    if ps_mx_val<=4:
        matrix_m_n[0][col] = sum(matrix_m_n[x][col] for x in range(ps_mx_val+1, m))

for str in matrix_m_n:
    print(str)





