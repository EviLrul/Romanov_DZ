# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода
# матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.temp_data = []

    def __str__(self):
        temp = ''
        for i in range(len(self.matrix)):
            temp = temp + str(self.matrix[i]) + '\n'
        return temp

    def __add__(self, other):
        temp_data = []
        for i in range(len(self.matrix)):
            temp_data.append([])
            for j in range(len(self.matrix[0])):
                temp_data[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(temp_data)


matrix_1 = Matrix([[3, 2, 1], [0, 1, 0], [1, 0, 1], [2, 2, 2]])
matrix_2 = Matrix([[1, 2, 3], [1, 0, 1], [0, 1, 0], [2, 2, 2]])
print(matrix_1)
print(matrix_2)
matrix_3 = matrix_1 + matrix_2
print('Итоговая матрица, после сложения:')
print(matrix_3)
