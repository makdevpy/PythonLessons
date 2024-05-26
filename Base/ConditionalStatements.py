# Условные операторы
# Оператор if...elif...else проверяет условие, и если оно истинно, выполняется блок кода под ним.

name = str(input("Enter your name: "))

if name == "Nikolay":
    print("Nikolay is great!")
elif name == "Vladimir":
    print("Vladimir is great!")
else:
    print("Пользователя с именем " + name + " не существует")