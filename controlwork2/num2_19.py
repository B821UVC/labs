'''В заданной матрице удалить все строки, содержащие нулевые элементы. Удаление строки оформить в виде метода.'''
import random
size_matrix = int(input("Введите размерность матрицы: ")) #предпочтительно указывать ранг 5 или 6, чтобы было шансов встретитьт ноль в строке
matrix = [[random.randint(0, 11) for x in range(size_matrix)] for y in range(size_matrix)]
print("Исхождная матрица:")
for i in range(size_matrix):
    print(matrix[i])


set_for_delets = set()
for i in range(size_matrix):
    for j in range(size_matrix):
        if matrix[i][j]==0:
            set_for_delets.add(i)
print("какие строки нужно удалить: ",set_for_delets)

k=0
for i in set_for_delets:
    matrix[i] = []
print("результат")
for i in range(size_matrix):
    print(matrix[i])