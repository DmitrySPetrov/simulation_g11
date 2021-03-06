# Задача №3:
# Сформировать массив вида:
#   ['a','b','c' ...]
# количество элементов должно быть равно N.
#
# Вариант решения №2, через превращение range() в массив
#
# =!!= Запускать с помощью Python3 =!!=

# Указываем количество
N = 10

# Создаем массив
A = [ chr( ord('a') + i ) for i in range(N) ]

# Выводим A
print( A )

# Пояснения:
# 1) range(N) создает последовательность 0,1,2,3...N-1
# 2) с точки зрения языка программирования, range(...) создает объект,
#    который будет превращаться в последовательность не сразу, а тогда,
#    когда его вызовут, в связи с чем перед range(...) стоит символ *
# 3) каждому символу сопоставлено число - его порядковый номер в кодовой
#    таблице
# 4) функция chr(...) возвращает символ, соответствующий своему коду
# 5) функция ord(...) возвращает код символа

