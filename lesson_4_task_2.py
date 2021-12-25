"""
Задание 2.
Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
П.С. задание не такое простое, как кажется
"""

# Так как время выполения скрипта не главное. Удалил замеры.(Так читабельнее)
# при оптимизации мы увеличиваем число итераций в два раза. Ввел переменные i, i1
# При каждой итерации мы меняем число. Таким образом повторяющихся ключей кэша не будет. Его использование не оправдано.
# Cначала запонили кэш, а потом вытащили значения по ключам, за такое же количество итераций 7 = 7(всего 14)
# cProfile не показывает выполнение собсственных функций, количество рекурсивных вызовов тоже нет. Все время = 0.000
import random
from random import randint
from cProfile import run


def recursive_reverse(number):
    global i
    if number == 0:
        i += 1
        return str(number % 10)
    i += 1
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


#
i = 0
num_100 = random.randint(10000, 10000)
num_100_reserve = recursive_reverse(num_100)
print(f'Не оптимизированная функция recursive_reverse числа')
print(f'Результат {num_100_reserve}   Число итераций - {i}')

run('recursive_reverse')


def memoize(f):
    cache = {}

    def decorate(*args):
        global i1
        if args in cache:
            i1 += 1
            return cache[args]
        else:
            i1 += 1
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    global i1
    if number == 0:
        i1 = i1 + 1
        return ''
    i1 = i1 + 1
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


i1 = 0
num_100_reserve1 = recursive_reverse_mem(num_100)
print(f'Результат {num_100_reserve1}   Число итераций - {i1}')
print(f'Оптимизированная функция recursive_reverse_mem числа')
run('recursive_reverse_mem')

