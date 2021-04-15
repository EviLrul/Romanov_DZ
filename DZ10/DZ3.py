# Осуществить программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и округление до целого числа деления клеток соответственно.
# - Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток.
# - Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если
# разность количества ячеек двух клеток больше нуля, иначе выводить
# соответствующее сообщение.
# - Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение
# количества ячеек этих двух клеток.
# - Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется
# как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса
# и количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
# между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
# В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
# Тогда метод make_order() вернёт строку: *****\n*****\n*****.


class Cell:
    def __init__(self, number_cells):
        self.number_cells = number_cells

    def __add__(self, other):
        return Cell(self.number_cells + other.number_cells)

    def __sub__(self, other):
        return Cell(self.number_cells - other.number_cells)

    def __mul__(self, other):
        return Cell(self.number_cells * other.number_cells)

    def __floordiv__(self, other):
        return Cell(self.number_cells // other.number_cells)

    def make_order(self, cell_1_number_cells, number_cells_in_row):
        temp = ''
        for i in range(cell_1_number_cells):
            if (i + 1) % number_cells_in_row == 0:
                temp = temp + '*\n'
            else:
                temp = temp + '*'
        return temp


cell_1 = Cell(8)
cell_2 = Cell(12)
cell_3 = Cell(23)
print('При сложении у новой клетки', (cell_1 + cell_2).number_cells, 'ячеек(и/а)')
# Проверка сделана здесь т.к. если будет такой код:
# def __sub__(self, other):
#     if self.number_cells - other.number_cells > 0:
#         return Cell(self.number_cells - other.number_cells)
#     else:
#         print('Операция вычитания с клетками не возможна!')
#
# cell_4 = cell_1 - cell_2
# print('У новой клетки', cell_4.number_cells, 'ячеек(и/а)')
#
# программа выводит сообщение и выпадает в ошибку. т.к. вот тут "cell_4 = cell_1 - cell_2"
# программа ожидает, что из метода мы вернём данные типа клетка, а мы при отрицательном
# результате ничего не возвращаем.
# Если честно я недодумался как это обойти, т.к. из методов нам нужно возвращать
# объект типа клетка. Но считаю, что это тоже вполне решение задачи.
if cell_1.number_cells - cell_2.number_cells > 0:
    print('При вычитании у новой клетки', (cell_1 - cell_2).number_cells, 'ячеек(и/а)')
else:
    print('\033[31mОперация вычитания с клетками не возможна!\033[0m')
print('При умножении у новой клетки', (cell_1 * cell_2).number_cells, 'ячеек(и/а)')
print('При делении у новой клетки', (cell_3 // cell_1).number_cells, 'ячеек(и/а)\n')
print('Колличество выводимых ячеек', cell_1.number_cells)
print(cell_1.make_order(cell_1.number_cells, 3))
