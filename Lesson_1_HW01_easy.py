#Шатский Максим Сергеевич

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

number=int(input("Введите любое число - "))
while number % 10 != 0:
    print(number % 10)
    number = number // 10


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

n = input("Введите значение первой переменной - ")
k = input("Введите значение второй переменной - ")
var = n
n = k
k = var
print("Значение переменной n - ", n)
print("Значение переменной k - ", k)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Введите свой возраст - "))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

