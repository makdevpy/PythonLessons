# Арифметические операторы. Для выполнения мат. операций
a1 = 10
b1 = 3

print(a1 + b1)  # 13
print(a1 - b1)  # 7
print(a1 * b1)  # 30
print(a1 / b1)  # 3.3333333333333335
print(a1 // b1) # 3
print(a1 % b1)  # 1
print(a1 ** b1) # 1000

# Операторы сравнения. Для сравнения значений и возвращения true/false

a2 = 9
b2 = 2

print(a2 == b2)  # False
print(a2 != b2)  # True
print(a2 > b2)   # True
print(a2 < b2)   # False
print(a2 >= b2)  # True
print(a2 <= b2)  # False

# Логические операторы. Работают только с булевыми значениями. Возвращаемый результат тоже true/false

a3 = True
b3 = False

print(a3 and b3)  # False
print(a3 or b3)   # True
print(not a3)     # False

# Комбинированные примеры
a4 = 10
b4 = 3
c4 = 5

# Использование арифметических операторов
result = (a4 + b4) * c4 / b4 - a4  # Результат: 5.666666666666667
print(result)

# Использование операторов сравнения
comparison = (a4 > b4) and (c4 < a4)  # Результат: True
print(comparison)

# Использование логических операторов
logic = not ((a4 + b4) > c4 or (b4 == c4))  # Результат: False
print(logic)
