# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

x1 = int(input('Введите X1: '))
y1 = int(input('Введите Y1: '))
x2 = int(input('Введите X2: '))
y2 = int(input('Введите Y2: '))

ki = (y2 - y1) / (x2 - x1)
bi = (x2*y1 - x1*y2) / (x2 - x1)


if ki == int(ki):
    ki = int(ki)

if ki == 0:
    kx = ''
elif ki == 1:
    kx = 'x'
elif ki == -1:
    kx = '-x'
else:
    kx = f'{ki}x'

if bi == int(bi):
    bi = int(bi)

if kx == '':
    b = f'{bi}'
else:
    if bi == 0:
        b = ''
    elif bi < 0:
        b = f'{bi}'
    else:
        b = f'+{bi}'


print(f'y={kx}{b}')
