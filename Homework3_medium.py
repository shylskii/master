n = int(input("Введите индекс первого элемента ряда Фибоначчи"))
m = int(input("Введите индекс последнего элемента ряда фибоначчи"))
def fibonacci(n, m):
    a = 0
    b = 1
    c = 0

    while c < m:
        a = a + b
        b = a - b
        c = c + 1
        if c >= n:
            print(a)
        else:
            continue


fibonacci(n, m)


def sort_to_max(li):
    j = 0
    i = 1
    while i < len(li):
        while j < (len(li) - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
            j += 1
        i += 1
        j = 0


li = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(li)
print(li)


def filter(fucnt, param_b):
    end_list = list()
    for x in param_b:
        if fucnt(x) == True:
            end_list.append(x)
        else:
            continue
    return end_list


print((filter((lambda x: x > 10), param_b=[1, 100, 500, 7, 8, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10])))