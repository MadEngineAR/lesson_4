"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
# Предложил вариант через divmod  так мы получаем сразу встроенной функцией и остаток и целую часть и сразу начинаем
# реверс числа, без доп. присваиваний, как в revers_1, revers_2. Метод среза строки reмers_3 самый медленный.
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    num_ro_revers, num = divmod(enter_num, 10)
    if enter_num == 0:
        return str(num)
    return str(num) + revers_4(num_ro_revers)


print(f'Время выполнения revers_1 - {timeit("revers_1", globals=globals())}')
print(f'Время выполнения revers_2 - {timeit("revers_2", globals=globals())}')
print(f'Время выполнения revers_3 - {timeit("revers_3", globals=globals())}')
print(f'Время выполнения revers_4 - {timeit("revers_4", globals=globals())}')
