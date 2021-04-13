# Реализовать базовый класс Worker (работник):
# - определить атрибуты: name, surname, position (должность), income (доход);
# - последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
# - создать класс Position (должность) на базе класса Worker;
# - в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

salary_grid = {'wage': 5000, 'bonus': 520}


class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = salary_grid


class Position(Worker):

    def get_full_name(self):
        print(self.surname, self.name, 'в должности', self.position)

    def get_total_income(self):
        print('Оклад и бонус', self._income['wage'] + self._income['bonus'],  'руб.')


position1 = Position('Сергей', 'Романов', 'Автоматизатор')
position1.get_full_name()
position1.get_total_income()
