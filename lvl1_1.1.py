# Задача 1.1.
# Есть строка с перечислением песен
my_favorite_songs = 'Waste a Moment, Stayin\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
#***************************************************************************************************************************************************
#Вариант №1 "В лоб"
print(my_favorite_songs.split(',')[0] + ',' + my_favorite_songs.split(',')[4] + ',' + my_favorite_songs.split(',')[1] + ',' + my_favorite_songs.split(',')[3])
#***************************************************************************************************************************************************
#Вариант №2 "через len()"
lastsongindex=len(my_favorite_songs.split(','))
print(my_favorite_songs.split(',')[0] + my_favorite_songs.split(',')[len(my_favorite_songs.split(','))])

