# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
class Car:
    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        print('Бр, Бр, Брррррррр... Поехали!')

    def stop(self):
        print('Вжжжжжж... Остановились!')

    def turn(self, direction):
        print(f'Поворачиваю {direction}.')


class TownCar(Car):
    def __init__(self, name):
        super().__init__('60', 'white', name, False)


class SportCar(Car):
    def __init__(self, name):
        super().__init__('180', 'red', name, False)


class WorkCar(Car):
    def __init__(self, name):
        super().__init__('40', 'gray', name, False)


class PoliceCar(Car):
    def __init__(self, name):
        super().__init__('120', 'blue', name, True)


police = PoliceCar('61')
police.go()
police.turn('налево')
police.stop()
