import random


# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
def make_person(name):
    return {'name': name, 'health': 100, 'damage': 25}

def attack(person1, person2):
    person2['health'] -= person1['damage']

player = make_person(input('Введите имя игрока: '))
enemy = make_person(input('Введите имя врага: '))


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
player['armor'] = 1.2
enemy['armor'] = 1.2

def damage(person1, person2):
    return person1['damage'] / person2['armor']

def attack2(person1, person2):
    person2['health'] -= damage(person1, person2)

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.
def save_person(person):
    with open(f'{person["name"]}.txt', 'w') as file:
        for k, v in person.items():
            file.write(f'{k}\t{v}\n')

save_person(player)
save_person(enemy)


def read_person(path):
    def castType(val):
        if val.count('.') == 1 and val.replace('.', '').isnumeric():
            return float(val)
        elif val.isnumeric():
            return int(val)
        else:
            return val

    with open(path) as file:
        splits = list(map(lambda line: line.replace('\n', '').split('\t'), file.readlines()))
        tuples = list(map(lambda split: (split[0], castType(split[1])), splits))
        return dict(tuples)


player = read_person(f'{player["name"]}.txt')
enemy = read_person(f'{enemy["name"]}.txt')
while player['health'] > 0 and enemy['health'] > 0:
    who = random.randint(-1, 1)
    if who == 1:
        print(f'{player["name"]} попадает ударом в {enemy["name"]}')
        attack2(player, enemy)
    elif who == -1:
        print(f'{enemy["name"]} попадает ударом в {player["name"]}')
        attack2(enemy, player)
    else:
        print('Оба промахиваются')

winner = player if player['health'] > 0 else enemy
print(f'Победил {winner["name"]}. У него осталось {int(winner["health"])}% здоровья.')
