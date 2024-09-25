
'''Привести заданную квадратную матрицу а размером n × к
такому виду, чтобы все элементы ниже главной диагонали были нуле-
выми. Использовать линейные преобразования (умножение строки на
число, сложение строк).'''

#by Gauss method
matrix_A = [
    [2,4,6],
    [8,4,9],
    [10,2,18],
]
n = 3

def get_nozero_elem_index(row:int, n:int, left_ps=0)->int:
    for i in range(left_ps,n):
        if matrix_A[row][i]!=0:
            left_ps_list[row] = i
            return i

def step1(row:int, n: int):
    first_val = matrix_A[row][row]
    matrix_A[row] = [matrix_A[row][i]/first_val for i in range(n)]

left_ps_list = [0]*n
def step2(row:int, n:int):  #зачем n
    left_ps = left_ps_list[row]
    first_no_zero_elem = matrix_A[row][row]
    for lower_row in range(row+1, n):
        left_ps = left_ps_list[lower_row]
        FirstAnyRowNoZeroElem = matrix_A[lower_row][row]
        coef = FirstAnyRowNoZeroElem/first_no_zero_elem
        matrix_A[lower_row] = [coef*matrix_A[row][i] - matrix_A[lower_row][i] for i in range(n)]
        left_ps_list[lower_row] = row+1


def is_triange_matrix():
    return 0

k=0
for i in range(n-1):
    step1(k, n)  
    step2(k, n)
    k+=1

for k in range(n):
    for i in range(n):
        try:
            check = 1000000/matrix_A[k][i]
        except:
            matrix_A[k][i] = 0
    print(matrix_A[k])






