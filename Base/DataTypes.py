"""
Переменные и типы данных
int - Целые числа представляют собой числа без дробной части. Они могут быть положительными, отрицательными или нулем.
float - Числа с плавающей точкой представляют собой числа с дробной частью.
str - Строки представляют собой последовательность символов, заключенных в одинарные или двойные кавычки.
list - Списки представляют собой упорядоченные изменяемые коллекции элементов.
tuple - Кортежи представляют собой упорядоченные неизменяемые коллекции элементов.
dict - Словари представляют собой неупорядоченные коллекции пар "ключ-значение".
set - Множества представляют собой неупорядоченные коллекции уникальных элементов.
"""
# ---int---
priceInt = 2
balanceInt = 10

summInt = priceInt + balanceInt
print("Сложение:", summInt)

subtraction = balanceInt - priceInt
print("Вычитание:", subtraction)

multi = balanceInt * priceInt
print("Умножение:", multi)

division = balanceInt / priceInt
print("Деление:", division)

intDiv = balanceInt // priceInt
print("Целочисленное деление:", intDiv)

remainder = balanceInt % priceInt
print("Остаток от деления:", remainder)

Exponentiation = priceInt ** priceInt
print("Возведение в степень:", Exponentiation)

# ---float---
priceFloat = 2.5
balanceFloat = 10.7

summFloat = priceFloat + balanceFloat
print("Сложение:", summFloat)

subtraction = balanceFloat - priceFloat
print("Вычитание:", subtraction)

multi = balanceFloat * priceFloat
print("Умножение:", multi)

division = balanceFloat / priceFloat
print("Деление:", division)

Exponentiation = priceFloat ** priceFloat
print("Возведение в степень:", Exponentiation)

# ---str---
name = "Nikolay"
city = "Moscow"

concatenation = name + city
print(concatenation)

repeat = name * 3
print(repeat)

accessByIndexStr = name[1]
print(accessByIndexStr)

# Срезы
slices = name[1:4]
print(slices)

# ---list---
ordersID = [1, 2, 3]
ordersNames = ["Заказ один", "Заказ два", "Заказ три"]

# Доступ к элементу списка по индексу
accessByIndexList = ordersID[0]
print(accessByIndexList)

# Изменение элемента списка
ordersNames[0] = "Заказ один (изменен)"
print(ordersNames)

# Добавление элемента в список
ordersID.append(4)
print(ordersID)

# Вставка элемента
ordersNames.insert(3, 15)
print(ordersNames)

# Удаление элемента
ordersNames.remove(15)
print(ordersNames)

# Длина списка
print(len(ordersID))
print(len(ordersNames))

# ---tuple - Кортежи---
tupleOne = (1, 2, 3, 4, 5)
tupleTwo = (6, 7)

# Доступ по индексу
print(tupleOne[0])

# Длина кортежа
print(len(tupleOne))

# Конкатенация
print(tupleOne + tupleTwo)

# --- dict - Словари ---

accounts = {
    "id": 1,
    "name": "Nikolay",
    "age": 27
}

# Доступ по ключу:
print(accounts["id"])
print(accounts["name"])

# Изменение значения
accounts["age"] = 30
print(accounts["age"])

# Добавление пары
accounts["job"] = "QA"
print(accounts)
# Удаление пары
accounts.pop("job")
print(accounts)
# Длина словаря
print(len(accounts))

# --- set - Множества ---

numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry", 1}

# Добавление элемента
numbers.add(61)
print(numbers)

# Удаление элемента
numbers.remove(61)
print(numbers)

# Объединение множеств
print(numbers.union(fruits))

# Пересечение множеств
print(numbers.intersection(fruits))

#  Разность множеств
print(numbers.difference(fruits))
