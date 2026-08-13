import random

def generate_matrix(rows, cols, low=-100, high=100):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(low, high))
        matrix.append(row)
    return matrix

def add_matrices(mat1, mat2):
 
    rows1 = len(mat1)
    cols1 = len(mat1[0]) if rows1 > 0 else 0
    rows2 = len(mat2)
    cols2 = len(mat2[0]) if rows2 > 0 else 0

    if rows1 != rows2 or cols1 != cols2:
        raise ValueError("Матрицы должны иметь одинаковую размерность")

    result = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result

def print_matrix(matrix, name="Матрица"):
    print(f"{name} ({len(matrix)}x{len(matrix[0])}):")
    for row in matrix:
        print(row)
    print()

rows, cols = int(input("Введите количество строк:")), int(input("Введите количество столбцов:"))

matrix_1 = generate_matrix(rows, cols, -100, 100)
matrix_2 = generate_matrix(rows, cols, -100, 100)

print_matrix(matrix_1, "Матрица 1")
print_matrix(matrix_2, "Матрица 2")

matrix_3 = add_matrices(matrix_1, matrix_2)

# Выводим результат
print_matrix(matrix_3, "Матрица 3 (сумма)")
