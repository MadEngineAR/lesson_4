"""Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
# Использовал функцию map(преобразовал список по количеству вхожений)
# Как callback Max. Затем при помощи генератора по максимальному значению вхождений, нахожу элемент array.
# Ускорить не удалось( хотя использовал встроенные фунции и генератор.
from timeit import timeit
array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    # c = list(map(array.count, array))
    # b = max(map(array.count, array))
    el = [el for el in array if array.count(el) == max(map(array.count, array))].pop()
    return f'Чаще всего встречается число {el} ' \
           f'оно появилось в массиве {max(map(array.count, array))} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(f'Время выполнения func_1 - {timeit("func_1", globals=globals())}')
print(f'Время выполнения func_2 - {timeit("func_2", globals=globals())}')
print(f'Время выполнения func_3 - {timeit("func_3", globals=globals())}')
