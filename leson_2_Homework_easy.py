#Шатский Максим Сергеевич


# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
 #1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: использует метод .format()
# Подсказка: воспользоваться методом .format()


fruitlist = ["яблоко","банан","киви","арбуз"]
i = 1
while i <= (len(fruitlist)):
    print('{0} {1} {2:>8}'.format(i,"",fruitlist[i-1]))
    i=i+1

 # Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

number=int(input("Введите желаемое число элементов списка - "))
i=0
list_1 = []
list_2 = []
#заполняем оба списка вводом с клавиатуры
while i <= (number - 1):
    list_1.append(input("Введите элемент 1го списка - "))
    list_2.append(input("Введите элемент 2го списка - "))
    i = i+1
#начинаем сравнение списков
i = 0
while i <= (number - 1):
    if list_1[i] == list_2[i]:
        list_1[i] = "элемент удален"
        # если удалять элемент функцей pop тот цикл падает так количество элементов массива становится разным, просьба дать комментарий по этому поводу
    i = i + 1
print("Измененный массив - ", list_1)

 # Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

number=int(input("Введите желаемое число элементов списка - "))
i=0
list_1 = []
list_2 = []
#заполняем список числами
while i <= (number - 1):
    list_1.append(int(input("Введите число 1го списка - ")))
    i = i+1
#начинаем проверку и заполнение ворого списка
i=0
while i <= (number - 1):
    if (list_1[i] % 2) != 0:
        list_2.append(list_1[i]*2)
    elif (list_1[i] % 2) == 0:
        list_2.append(list_1[i]/4)
    i = i + 1
print("Измененный массив - ", list_2)