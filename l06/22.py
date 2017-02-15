# Задача №2:
# Сформировать массив вида:
#   [1,0,1,0,0,1,0,0,0,1,0,0,0,0,1 ...]
# количество элементов должно быть таким, чтобы массив начинался и заканчивался
# единицей, а всего единиц было N.
#
# Вариант решения №2, через превращение range() в массив
#
# =!!= Запускать с помощью Python3 =!!=

# подключаем стандартную функцию для объединения массивов
from itertools import chain

# Указываем количество
N = 10

# Создаем массив
A = [ *chain( *( [0]*i+[1] for i in range(N) ) ) ]

# Выводим A
print( A )

# Пояснения:
# 1) range(1,N+1) создает последовательность 1,2,3...N
# 2) с точки зрения языка программирования, range(...) создает объект,
#    который будет превращаться в последовательность не сразу, а тогда,
#    когда его вызовут, в связи с чем перед range(...) стоит символ *
# 3) оператор * означает команду "преврати объект в последовательность"
#    например, *[1,2,3] превратит просто в последовательность 1,2,3
#    range(1,N+1) также разворачивается в последовательность по этой команде
# 4) здесь подключается функция chain из стандартной библиотеки itertools
# 5) функция chain здесь эквивалентна функции sum: она объединяет все массивы,
#    которые указали внутри нее,
#    отличия в том, что в sum мы передаем последовательность, которая содержит
#    элементы, которые надо просуммировать,
#    а в chain - переменные, которые надо объединить

