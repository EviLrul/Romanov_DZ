# Реализуйте базовый класс Car:
# - у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# - добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# - для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
# к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Едем')

    def stop(self):
        print('Стоим')

    def turn(self):
        print('Повернули')

    def show_speed(self):
        print('Скорость авто', self.speed, 'км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Для TownCar допустима скорочть 60км/ч, у вас превышение на', self.speed - 60, 'км/ч')
        else:
            print('Скорость авто TownCar', self.speed, 'км/ч')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Для WorkCar допустима скорочть 60км/ч, у вас превышение на', self.speed - 40, 'км/ч')
        else:
            print('Скорость авто WorkCar', self.speed, 'км/ч')


class SportCar(Car):

    def info(self):
        pass


class PoliceCar(Car):

    def init(self):
        self.is_police = True


police = PoliceCar(61, 'red', 'Kalina')
print(PoliceCar.__name__)
police.show_speed()
work_car = WorkCar(42, 'green', 'Datsun')
work_car.show_speed()
town_car = TownCar(58, 'green', 'BMW')
town_car.show_speed()
sport_car = SportCar(94, 'Black', 'Lada')
print(SportCar.__name__)
sport_car.show_speed()
