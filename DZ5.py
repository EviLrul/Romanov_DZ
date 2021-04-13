# Реализовать класс Stationery (канцелярская принадлежность):
# - определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# - создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# - в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# - создать экземпляры классов и проверить, что выведет описанный метод
# для каждого экземпляра.

class Stationery:
    title = 'Пишуший инструмент'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Ручкой')


class Pencil(Stationery):

    def draw(self):
        print('Карандашом')


class Handle(Stationery):

    def draw(self):
        print('Маркером')


tool = Stationery()
tool.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
