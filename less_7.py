'''
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
'''

#
# class Matrix:
#
#     def __init__(self, mx_ls):
#
#         # свойство будет содержать данные матрицы (список списков)
#         self.data = mx_ls
#
#         # получим размерность матрицы, вычислив количество элементов в основном списке i и в первом вложенном списке j
#         # предпологается, что размерностьэлементов списка корректна, все вложенные списки имеют одинаковый размер
#
#         # свойство будет содержать размерность матрицы в виде кортежа (i, j)
#         self.dim = (len(mx_ls), len(mx_ls[0]))
#
#     def __str__(self):
#
#         # зададим строковое представление
#         st = ''
#         for i in self.data:
#             st += '| '      # визуальные границы строк
#             for j in i:
#                 st += f'{j} '
#             st += '|\n'     # визуальные границы строк
#
#         return st
#
#     def __add__(self, other):
#
#         # убедимся, что размерности складываемых матриц одинаковы
#         if self.dim[0] == other.dim[0] and self.dim[1] == other.dim[1]:
#
#             # содзадим список списков с суммами поэлементно
#             mx_ls = [[self.data[j][i] + other.data[j][i] for i in range(self.dim[1])] for j in range(self.dim[0])]
#
#             # создадим результирующую матрицу
#             add_mtx = Matrix(mx_ls)
#             return add_mtx
#         else:
#             print('Складываемые матрицы разного размера')
#             return ValueError
#
# # содзадим матрицы для проверки
#
# m_ls1 = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
#
# m_ls2 = [
#     [1, 1, 1],
#     [1, 1, 1]
# ]
#
# m_ls3 = [
#     [1, 2],
#     [3, 4],
#     [5, 6],
#     [7, 8],
# ]
#
# mrx1 = Matrix(m_ls1)
# mrx2 = Matrix(m_ls2)
#
# print(mrx1 + mrx2)


'''
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: 
для пальто (V/6.5 + 0.5), 
для костюма (2*H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
#
# from abc import ABC, abstractmethod
#
#
# # Зададми константу, содержащую типы одежды
# DRESS_TYPES = ['Пальто', 'Костюм']
#
#
# class Dress(ABC):
#     # тип и размер одежды будет задаваться сразу в родителе
#     @abstractmethod
#     def __init__(self, type: str, size: [int, float]):
#         self.type = type
#         self.size = size
#
#     # заготовку метода для расчета расхода материала зададим в родителе,
#     # а в потомках метод будет дополняться характерными типу формулами расчета
#     @abstractmethod
#     def expend(self):
#         return f'Расход материала на {self.type} {self.size} размера - '
#
# class Coat(Dress):
#     def __init__(self, type: str, size: int):
#         super().__init__(type, size)
#
#     # метод для расчета расхода представим как свойство
#     @property
#     def expend(self):
#         st = super().expend() + f'{round((self.size / 6.5) + 0.5, 2)}'
#         return st
#
#
# class Costume(Dress):
#     def __init__(self, type: str, size: float):
#         super().__init__(type, size)
#
#     # метод для расчета расхода представим как свойство
#     @property
#     def expend(self):
#         st = super().expend() + f'{round((2 * self.size) + 0.3, 2)}'
#         return st
#
#
# # Пальто 48-го размера
# coat_1 = Coat(DRESS_TYPES[0], 48)
# print(coat_1.expend)
#
# # костюм, на рост 170 см
# costume_1 = Costume(DRESS_TYPES[1], 17)
# print(costume_1.expend)