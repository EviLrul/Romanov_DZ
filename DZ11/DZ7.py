# Реализовать проект «Операции с комплексными числами».
# Создать класс «Комплексное число». Реализовать перегрузку методов сложения
# и умножения комплексных чисел. Проверить работу проекта. Для этого создать
# экземпляры класса (комплексные числа), выполнить сложение и умножение
# созданных экземпляров. Проверить корректность полученного результата.
# (a+bi)+(c+di)=(a+c)+(b+d)i
# (a+bi)(c+di)=(ac−bd)+(ad+bc)i
class ComplexNumbers:
    def __init__(self, a, b_i):
        self.a = a
        self.b_i = b_i

    def __add__(self, other):
        return ComplexNumbers(self.a + other.a, self.b_i + other.b_i)

    def __mul__(self, other):
        return ComplexNumbers((self.a * other.a) - (self.b_i * other.b_i), (self.a * other.b_i) + (self.b_i * other.a))

    def __str__(self):
        temp = 'Ваше комплексное число: ' + str(self.a) + '+' + str(self.b_i) + 'i'
        return temp


complex_num_1 = ComplexNumbers(2, 2)
complex_num_2 = ComplexNumbers(3, 1)
complex_num_3 = complex_num_1 + complex_num_2
print(complex_num_1)
print(complex_num_2)
print('После сложения:', complex_num_3)
complex_num_4 = complex_num_1 * complex_num_2
print('После умножения:', complex_num_4)
