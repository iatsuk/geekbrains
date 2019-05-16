# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple, defaultdict

Organization = namedtuple('Organization', 'name, quarter1, quarter2, quarter3, quarter4')


def organization_profit(org):
    return org.quarter1 + org.quarter2 + org.quarter3 + org.quarter4


# заполняем данные
n = int(input('Введите количество компаний: '))
organizations = []
for _ in range(n):
    name = input('Название компании: ')
    quarter1, quarter2, quarter3, quarter4 = (int(input(f'Введите прибыль за {i + 1} квартал: ')) for i in range(4))
    organizations.append(Organization(name, quarter1, quarter2, quarter3, quarter4))

# считаем среднее
average_profit = sum([organization_profit(org) for org in organizations]) / len(organizations)

# считаем статистику и выводим ответ
stat = defaultdict(list)
for org in organizations:
    stat[organization_profit(org) > average_profit].append(org.name)
print('Предприятия с прибылью выше среднего:', stat[True])
print('Предприятия с прибылью ниже среднего:', stat[False])
