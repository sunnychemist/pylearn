def coincide(a,b):
    '''Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно
    как в первом списке, так и во втором.'''
    print(len(a.intersection(b)))

coincide({1, 2, 6, 4, 5, 7}, {10, 2, 3, 4, 8})