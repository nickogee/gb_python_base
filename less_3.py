'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

# def div(chis, znam):
#     '''
#     функция возвращает результат деления числителя (chis) на знаменатель (znam)
#     :param chis: -> int
#     :param znam: -> int
#     :return: -> float
#     '''
#     return chis/znam
#
#
# # Запросим у пользователя "числитель" и "знаменатель"
# # Проверку на корректность введенных пользователем значений произведем до вызова ф-ии,
# # чтобы у пользователя была возможность заново ввести корректные значения
#
# correct = False     # Переменная будет хранить признак корректности введенных данных
# while not correct:
#     a, b = int(input('Введите числитель\n')), int(input('Введите знаменатель\n'))
#     correct = (b != 0)
#     if not correct:
#         print('Знаменатель не может быть равным нулю')
#     else:
#         print(f'{a} / {b} = ', div(a, b), sep='')

'''
2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Осуществить вывод данных о пользователе одной строкой.
'''

# def in_one_string(name, scd_name, year, city, email, phone):
#     '''
#     функция соберает данные пользоватея в одну строку
#     :param name: -> (str) Имя
#     :param scd_name: -> (str) Фамилия
#     :param year: -> (int) Год рождения
#     :param city: -> (str) Город проживания
#     :param email: -> (str) Адрес почты
#     :param phone: -> (str) Номер телефона
#     :return: -> (str)
#     '''
#     return f'Имя - {name.capitalize()}, ' \
#            f'Фамилия - {scd_name.capitalize()}, ' \
#            f'год рождения - {year}, ' \
#            f'город проживания - {city}, ' \
#            f'адрес почты - {email}, ' \
#            f'номер телефона - {phone}.'
#
#
# # распечатаем результат вызова ф-ии
# print(in_one_string(name='Владимир',
#                     scd_name='Рогов',
#                     year=1976, city='Гонконг',
#                     email='vlad@mail.ru',
#                     phone='+9-2763-345-76-89'))


'''
3. Реализовать функцию my_func(), 
которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
'''

# def sum_tow_max(arg1, arg2, arg3):
#     '''
#     среди переданных аргументов находятся два наибольших, возвращается их сумма
#     :param arg1: -> (int, float)
#     :param arg2: -> (int, float)
#     :param arg3: -> (int, float)
#     :return: -> (int, float)
#     '''
#
#     # поместим аргументы в список, и отсортерруем
#     ls = [arg1, arg2, arg3]
#     ls.sort()
#
#     # два наибольших аргумента будут в конце списка
#     return sum(ls[1:])
#
# a = 34
# b = 67
# c = 28
# print(f'Переданы значения: {a}, {b}, {c}', f'сумма двух наибольших: {sum_tow_max(a, b, c)}', sep='\n')

'''
4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). 
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
'''

# def num_exp(num, exp, by_cycle=False):
#     '''
#     возводит число num в степень exp и возвращает полученное знчение.
#     by_cycle - признак реализации с помощю цикла
#     :param num: -> (float)
#     :param exp: -> (int)
#     :param by_cycle: -> (bool)
#     :return: -> (float)
#     '''
#
#     if not by_cycle:        # реализация оператором **
#         return num ** exp
#     else:                   # реализация с помощю цикла
#         rez = 1
#         for i in range(1, exp+1):
#             rez *= num
#         return rez
#
#
# a = 3
# b = 4
#
# print(f'С помощю оператора: {a} в степени {b} = {num_exp(a, b)}')
# print(f'С помощю цикла: {a} в степени {b} = {num_exp(a, b, by_cycle=True)}')


'''
5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. 
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме 
и после этого завершить программу.
'''

# # Введем константу, которая будет признаком завершения работы программы
# DONE_SIGN = 'q'
#
#
# def append_end_summ_list(ls):
#     '''
#     функция получает нв вход список чисел, элементы списка добаваляет в глобальный список num_list и считает сумму
#     чисел в обновленном глобальном списке, которую возвращает
#     :param ls: -> (list)
#     :return: -> (int)
#     '''
#     global num_list
#
#     num_list.extend(ls)
#     return sum(num_list)
#
#
# # создадим список, в котором будут помещатся вводимые пользователем значения
# num_list = []
#
# # признак того, что ввод значений нужно прекратить
# done = False
#
# while not done:
#     inp_str = input(f'Введите числа, разделенные пробелом для подсчета их суммы или "{DONE_SIGN}" для завершения\n')
#
#     # Разобьем полученную от пользователя строку по разделителю, преобразуем в список
#     curr_ls = inp_str.split(' ')
#
#     # если в веденном списке чисел есть DONE_SIGN - удалим его и возведем признак завершения ввода в True
#     if DONE_SIGN in curr_ls:
#         curr_ls.remove(DONE_SIGN)
#         done = True
#
#     # преобразуем значения списка в int
#     curr_ls = [int(i) for i in curr_ls]
#     print(f'Сумма всех введенных чисел - {append_end_summ_list(curr_ls)}')

'''
6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв 
и возвращающую их же, но с прописной первой буквой.
'''

def int_func(text):
    '''
    принимаtn слова из маленьких латинских букв
    и возвращающую их же, но с прописной первой буквой
    :param text: -> (str)
    :return: -> (str)
    '''
    return text.capitalize()

print(int_func('hello'))