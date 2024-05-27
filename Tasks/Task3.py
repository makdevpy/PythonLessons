"""
Задача 3: Обратный отсчет
Напишите программу, которая запрашивает у пользователя целое положительное число N и выполняет обратный отсчет от N до 1, выводя каждое число на новой строке. После окончания отсчета программа должна вывести "Пуск!".
"""

def getUserNumber():

    while True:

        userNumber = int(input("Введите положительное число: "))

        if userNumber > 0:
            break
        print("Число должно быть больше нуля")

    while userNumber > 0:

        print(f"{userNumber}...")
        userNumber -= 1

        if userNumber == 0:
            print("Пуск!")

getUserNumber()