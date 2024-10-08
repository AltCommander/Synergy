import random

#Указываем размерность матриц в диапазоне [min_size : max_size]
min_size = 1
max_size = 20
rows = random.randint(min_size, max_size)
cols = random.randint(min_size, max_size)

#Создаём 2 матрицы из случайных чисел в диапазоне [x : y]
x = -200
y = 200
matrix_1 = [[random.randint(x, y) for i in range(cols)] for i in range(rows)]
matrix_2 = [[random.randint(x, y) for i in range(cols)] for i in range(rows)]

#Создаём пустую матрицу, в которую будет складывать две другие

result_matrix = [[0 for i in range(cols)] for i in range(rows)]

#Складываем две матрицы поэлементно
for i in range(rows):
    for j in range(cols):
        result_matrix[i][j] = matrix_1[i][j] + matrix_2[i][j]

#Выводим результирующую матрицу
for row in result_matrix:
    print(row)