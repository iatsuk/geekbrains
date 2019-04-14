# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Toy:
    def __init__(self, kind):
        self.name = None
        self.color = None
        self._kind = kind

    def __str__(self):
        return f'Игрушка {self.name}, цвет {self.color}, тип {self._kind}'


class Bear(Toy):
    def __init__(self):
        super().__init__('медвежонок')


class Car(Toy):
    def __init__(self):
        super().__init__('машинка')


class Factory:
    def _make(self, kind):
        print(f'Готовлю производственные мощности для типа {kind}')
        if kind == 'машинка':
            return Car()
        elif kind == 'медвежонок':
            return Bear()
        else:
            return Toy(kind)

    def _naming(self, toy, name):
        print(f'Заказываю материалы для {name}')
        toy.name = name

    def _paint(self, toy, color):
        print(f'Окрашиваю в {color}')
        toy.color = color

    def make_toy(self, name, color, kind):
        toy = self._make(kind)
        self._naming(toy, name)
        self._paint(toy, color)
        return toy


toy_factory = Factory()
toy = toy_factory.make_toy(name='Тедди', color='желтый', kind='медвежонок')
print(toy, 'готова.')
