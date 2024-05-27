"""
Задача 2: Угадай число
Напишите игру "Угадай число". Программа случайным образом выбирает число от 1 до 100. Пользователь должен угадать это число, вводя свои предположения. Программа должна подсказывать, больше или меньше загаданное число. Игра продолжается до тех пор, пока пользователь не угадает число.
"""
import random

def guessTheNumber():
    randomNumber = random.randint(1, 100)
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        userNumber = int(input("Введи число: "))

        if userNumber > randomNumber:
            print("Меньше!")

        elif userNumber < randomNumber:
            print("Больше!")

        else:
            print("Поздравляю, Вы угадали число!")
            break

guessTheNumber()