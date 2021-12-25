"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
# Применил LC. Но в сочетании с условием if разница с append ничтожна 0,0001. Иногда даже append быстрее.
# Хотя не должен.
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Вариант 2 - LC
def test_lst_comp(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


print(f'Время выполнение func_1(nums) - {timeit("func_1", globals=globals())}')
print(f'Время выполнение test_lst_comp(nums) - {timeit("test_lst_comp", globals=globals())}')

