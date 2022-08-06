'''
п. 1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

# #Создадим список с эл-ми различного типа
# ls = [23, 'ddd', False, 47.8, [8, 6], ('e',), None]
#
# #Проверим и выведем типы эл-ов списка
# for i in ls:
#     print(type(i))

'''
п. 2. Для списка реализовать обмен значений соседних элементов. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. 
При нечётном количестве элементов последний сохранить на своём месте. 
Для заполнения списка элементов нужно использовать функцию input().
'''

# запросим у пользователя значения эл-ов списка, в качестве разделителя эл-ов должна быть ","
st_inpt = input('задайте набор эл-ов для списка. Элементы должны отделяться символом ","\n')

# Разобьем полученную от пользователя строку по разделителю, преобразуем в список
raw_ls = st_inpt.split(',')

# пользователь наверняка вводил пробелы после "," Удалим пробелы в начале и концеэ лементов,
# проигнорируем "пустые" эл-ты (состоящие только из пробелов)
ls = [st.replace(' ', '') for st in raw_ls if st.replace(' ', '')]

print(f'список до замены значений\n{ls}')

# Получем последний индекс, для которого можно производить замену значений (четный)
end_ind = (len(ls)-1, len(ls))[len(ls) % 2 == 0]

# замена "соседних" значений
for ind in range(0, end_ind, 2):
    ls[ind+1], ls[ind] = tuple(ls[ind: ind+2])

print(f'список после замены значений\n{ls}')
