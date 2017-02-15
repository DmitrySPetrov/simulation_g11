# Задача №4:
# Нарисовать контуры шахматной доски в псевдографике
#
# =!!= Запускать с помощью Python3 =!!=

# формируем строку
s = ' ' + ' _'*8 + '\n' \
    + '\n'.join( str(8-i)+'|_'*8+'|' for i in range(8) ) + '\n' \
    + '  ' + ' '.join( chr( ord('a')+j ) for j in range(8) )

# Выводим A
print( s )

# Пояснения:
# 1) A.join(...) - это метод для строки A.
#    Обозначает "соедини все строки, указанные внутри join(...), при помощи строки A"
#    Примеры:
#      ' '.join( '1', '2', '3' ) вернет строку '1 2 3'
#      '+'.join( 'a', 'b', 'c' ) вернет строку 'a+b+c'
# 2) str(...) - функция для преобразования указанного внутри объекта в строку
#    здесь в строку преобразуется число

