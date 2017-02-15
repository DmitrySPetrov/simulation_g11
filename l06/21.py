# Задача №2:
# Сформировать массив вида:
#   [1,0,1,0,0,1,0,0,0,1,0,0,0,0,1 ...]
# количество элементов должно быть таким, чтобы массив начинался и заканчивался
# единицей, а всего единиц было N.
#
# Вариант решения №1, через цикл for
#
# =!!= Запускать с помощью Python3 =!!=

# Указываем количество
N = 10

# Создаем новый пустой массив
A = []

# В цикле дополняем массив...
for i in range(N):
    A += [0] * i + [1]

# Выводим A
print( A )

# Пояснения:
# 1) массивы можно складывать между собой:
#    [12] + [15] == [12,15]
# 2) оператор += означает увеличение левого операнда на правый, например:
#    a += 1 эквивалентно a = a + 1 увеличит a на единицу
#    A += [i] эквивалентно A = A + [i]
# 3) range(N) возвращает последовательность 0,1,2...N-1
# 4) указанный здесь цикл for выполнится следующим образом:
#    операторы, указанные внутри цикла, будут выполнены для всех i=0,1...N-1
