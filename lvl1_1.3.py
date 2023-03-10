# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!
error=False
m = input("Введите номер месяца ")

from calendar import monthrange
if int(m)>0 and int(m)<=12:
    days=monthrange(2023, int(m))
else: error=True

match m.split():
    case ["1"]:  
        print("Вы ввели январь.")
    case ["2"]:  
        print("Вы ввели февраль.")
    case ["3"]:  
        print("Вы ввели март.")
    case ["4"]:  
        print("Вы ввели апрель.")
    case ["5"]:  
        print("Вы ввели май.")
    case ["6"]:  
        print("Вы ввели июнь.")
    case ["7"]:  
        print("Вы ввели июль.")
    case ["8"]:  
        print("Вы ввели август.")
    case ["9"]:  
        print("Вы ввели сентябрь.")
    case ["10"]:  
        print("Вы ввели октябрь.")    
    case ["11"]:  
        print("Вы ввели ноябрь.")    
    case ["12"]:  
        print("Вы ввели декабрь.")    
    case _:
        print(f"Такого месяца нет!")
        error=True

if error!=True:
    print(days[1],'дней')

