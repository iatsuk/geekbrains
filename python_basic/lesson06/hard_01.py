# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.


class Toy:
    def __init__(self):
        self.name = None
        self.color = None
        self.kind = None

    def __str__(self):
        return f'Игрушка {self.name}, цвет {self.color}, тип {self.kind}'


class Factory:
    def _naming(self, toy, name):
        print(f'Заказываю материалы для {name}')
        toy.name = name

    def _sew(self, toy, kind):
        print(f'Шью {kind}')
        toy.kind = kind

    def _paint(self, toy, color):
        print(f'Окрашиваю в {color}')
        toy.color = color

    def make_toy(self, name, color, kind):
        toy = Toy()
        self._naming(toy, name)
        self._sew(toy, kind)
        self._paint(toy, color)
        return toy


toy_factory = Factory()
toy = toy_factory.make_toy(name='Чебурашка', color='коричневый', kind='мягкая игрушка')
print(toy, 'готова.')

