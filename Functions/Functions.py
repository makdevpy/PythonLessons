# Функции, которые возвращают значения, обычно предпочтительнее, потому что они позволяют решать, что делать с возвращаемым значением. Это хороший тон написания функций.
def greetings(name):
    return f"Привет, {name}!"

print(greetings("Nikolay"))

# Локальные и глобальные переменные

name = "Nikolay"

def myName():
    name = "!Nikolay"
    print("Внутри функции", name)

myName()
print(name)

age = 20

def myAge():
    global age
    age = 25
    print("Внутри функции", age)

myAge()
print("Вне функции", age)