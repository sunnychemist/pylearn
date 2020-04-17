'''Обувная фабрика собирается начать выпуск элитной модели ботинок. Дырочки для шнуровки будут расположены в два ряда,
расстояние между рядами равно a, а расстояние между дырочками в ряду b. Количество дырочек в каждом ряду равно N.
Шнуровка должна происходить элитным способом “наверх, по горизонтали в другой ряд, наверх, по горизонтали и т.д.” (см.
рисунок). Кроме того, чтобы шнурки можно было завязать элитным бантиком, длина свободного конца шнурка должна быть l

. Какова должна быть длина шнурка для этих ботинок?

Программа получает на вход четыре натуральных числа a
, b, l и N - именно в таком порядке - и должна вывести одно число - искомую длину шнурка.'''


def shoe_laces(a, b, l, n):
    length = (a + b) * 2 * n + l - a
    print(length)


# shoe_laces(2, 1, 3, 4)

'''Задача «Знак числа»
Условие
В математике функция sign(x) (знак числа) определена так:
sign(x) = 1, если x > 0,
sign(x) = -1, если x < 0,
sign(x) = 0, если x = 0.

Для данного числа x выведите значение sign(x). Эту задачу желательно решить с использованием каскадных инструкций if...
elif... else. '''


def sign_x(x):
    if x > 0:
        print('1')
    elif x < 0:
        print('-1')
    else:
        print('0')


sign_x(0)

'''Задача «Шахматная доска»
Условие
Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO.
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой
клетки, потом для второй клетки. '''


def chess(x1, y1, x2, y2):
    if (x1 + y1) % 2 == 0:
        cell1 = True
    else:
        cell1 = False
    if (x2 + y2) % 2 == 0:
        cell2 = True
    else:
        cell2 = False
    if cell1 == cell2:
        print('Клетки одного цвета')
    else:
        print('Клетки разного цвета')


chess(1, 1, 2, 6)


def cell(x, y):
    if (x + y) % 2 == 0:
        return True
    else:
        return False


def chess2(x1, y1, x2, y2):
    cell1 = cell(x1, y1)
    cell2 = cell(x2, y2)
    if cell1 == cell2:
        print('Клетки одного цвета')
    else:
        print('Клетки разного цвета')


chess2(1, 1, 2, 6)
