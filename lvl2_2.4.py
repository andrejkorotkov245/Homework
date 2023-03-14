# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"
s = "Hi! Hello!"
s1 = "Oh, no!!!"
s2 = ""
def remove_exclamation_marks(s):
    s = s.replace('!', '')
    return s

print(remove_exclamation_marks(s))
print(remove_exclamation_marks(s1))
print(remove_exclamation_marks(s2))


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"
s3 = "Hi!!!"

len = len(s3)

def split(s): #Функция разбиения строки в список
    return [char for char in s]

def remove_last_em(s): #Функция удаления последнего знака !
    splitted = (split(s))
    if splitted[len-1] == '!':
        splitted.pop(len-1)
    return(''.join(splitted))

print(remove_last_em(s3)) #Выводим результат

               

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    pass