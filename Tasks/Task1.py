"""
Задача 1: Сумма чисел
Напишите программу, которая запрашивает у пользователя числа и находит их сумму. Окончание ввода чисел должно быть обозначено вводом нуля.
"""

def summ():
    total = 0  # Счётчик (начальное положение)

    while True:  # Бесконечный цикл, пока пользователь не введёт 0
        value = int(input("Введи число: "))  # Ввод чисел

        if value == 0:  # Если ввели 0, то
            break  # выходим из цикла

        total += value  # Обновляем переменную total каждый раз, когда вводили не 0

    return total  # Возвращается значение total

print(summ())