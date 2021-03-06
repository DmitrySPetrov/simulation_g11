# Задача №2:
# Сформировать словарь, ключами которого являются квадраты чисел с шагом 0.01,
# а значениями - кубический корень из ключа
#
# Вариант решения №1, через цикл for
#
# =!!= Запускать с помощью Python3 =!!=

# Печатать словарь будем функцией pprint
from pprint import pprint

# Количество элементов
N = 50

# Создаем пустой словарь
A = {}

# В цикле дополняем словарь
for i in range( N ):
    key = ( i * 0.01 )**2
    A[ key ] = key**(1/3)

# Выводим словарь
pprint( A )

# Пояснения:
# 1) range(N) возвращает последовательность 0,1,N-1
# 2) указанный здесь цикл for выполнится следующим образом:
#    операторы, указанные внутри цикла, будут выполнены для всех i=0,1...N-1
# 3) оператор a**b возвращает число a в степени b

