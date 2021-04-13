# Создать класс TrafficLight(светофор):
# - определить у него один атрибут color(цвет) и метод running(запуск);
# - атрибут реализовать как приватный;
# - в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# - продолжительность первого состояния(красный) составляет 7 секунд,
# второго(жёлтый) — 2 секунды, третьего(зелёный) — на ваше усмотрение;
# - переключение между режимами должно осуществляться только в указанном
# порядке(красный, жёлтый, зелёный);
# - проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить
# соответствующее сообщение и завершать скрипт.
import time


class Three_eyed:
    __three_eyed_color = ''

    def three_eyed_work(self):
        while True:
            Three_eyed.__three_eyed_color = 'Red'
            print("\033[31m {}" .format('Горит ' + Three_eyed.__three_eyed_color))
            time.sleep(7)
            Three_eyed.__three_eyed_color = 'Yellow'
            print("\033[33m {}" .format('Горит ' + Three_eyed.__three_eyed_color))
            time.sleep(2)
            Three_eyed.__three_eyed_color = 'Green'
            print("\033[32m {}" .format('Горит ' + Three_eyed.__three_eyed_color))
            time.sleep(5)


traffic_light1 = Three_eyed()
traffic_light1.three_eyed_work()
