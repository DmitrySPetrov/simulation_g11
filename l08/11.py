# Задача №1:
# Запросить ввод строки, вывести развернутую строку
#
# Вариант решения №1, через цикл for
#
# =!!= Запускать с помощью Python3 =!!=

# Вводим строку
sinp = input( 'Введите строку ' )

# Строка-результат
sout = ''

# В цикле дополняем словарь
for i in range( len( sinp ) ):
	sout += sinp[-1-i]

# Выводим результат
print( sout )

