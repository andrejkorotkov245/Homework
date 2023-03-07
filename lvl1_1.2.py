# Задача 1.2. 

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
total=0.00
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random
rndsongs=random.sample(my_favorite_songs,3)
print('Случайно выбранные песни из списка:')
for i in range(3):
    print (rndsongs[i][1])
    total=total + rndsongs[i][1]
print ("Случайно выбранные песни из списка звучат:", round(total,2), 'минут')
#********************************************************************************************************************    
print('\n')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
total=0.00
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Stayin\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

rndsongs=random.sample(list(my_favorite_songs_dict.values()),k=3)
print('Случайно выбранные песни из словаря:')

for i in range(3):
    print(rndsongs[i])
    total=total+rndsongs[i]
print('Случайно выбранные песни из словаря звучат:',round(total,2),'минут')
