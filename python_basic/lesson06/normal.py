# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random


class Person:
    def __init__(self, name, health, damage, armor):
        self._name = name
        self._health = health
        self._damage = damage
        self._armor = armor

    def _taken_damage(self, damage):
        return damage / self._armor

    def injury(self, damage):
        if damage > 0:
            self._health -= self._taken_damage(damage)
            print(f'...{self._name} получил {int(self._taken_damage(damage))} урона. У него {int(self._health)} жизни.')

    def attack(self, person):
        print(f'{self._name} атакует...')
        person.injury(self._damage)

    def is_life(self):
        return self._health > 0

    def get_name(self):
        return self._name


class Player(Person):
    def __init__(self, name):
        super().__init__(name, 100, 25, 1.2)


class Enemy(Person):
    def __init__(self):
        super().__init__('Орк', 120, 20, 1)


class Game:
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def _battle(self):
        while self._player.is_life() and self._enemy.is_life():
            if random.randint(0, 1) == 1:
                self._player.attack(self._enemy)
            else:
                self._enemy.attack(self._player)

    def _print_winner(self):
        if self._player.is_life():
            print(f'Победил {self._player.get_name()}.')
        elif self._enemy.is_life():
            print(f'Победил {self._enemy.get_name()}.')
        else:
            print('Война никого не щадит.')

    def start(self):
        self._battle()
        self._print_winner()


player = Player(input('Введите имя:'))
enemy = Enemy()
game = Game(player, enemy)
game.start()
