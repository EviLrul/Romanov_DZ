# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByZeroException:
    def __init__(self, num_1=5, num_2=5):
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def definition(num_1, num_2):
        if num_2 == 0:
            result = 'Делить на ноль нельзя!'
        else:
            result = num_1 / num_2
        return result


print('Введите два числа:')
experiment = DivisionByZeroException.definition(int(input()), int(input()))
print('Итог деления:', experiment)
