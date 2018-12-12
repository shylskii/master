
import os
import homework5_easy

exitos = 'a'
while exitos != '0':
    print('Перейти в папку - 1')
    print('Просмотреть содержимое текущей папки - 2')
    print('Удалить папку - 3')
    print('Создать папку - 4')
    print('для выхода - 0')
    exitos = input('Выбрать: ')
    print(exitos)
    if exitos == '1':
        dir_name = input('Введите полный путь папки: ')
        hemowork5_easy.change_dir(dir_name)
    elif exitos == '2':
        dir_name = os.getcwd()
        hemowork5_easy.list_dir(dir_name)
    elif exitos == '3':
        dir_name = input('Введите полный путь папки: ')
        hemowork5_easy.delete_dir(dir_name)
    elif exitos == '4':
        dir_name = input('Введите полный путь папки: ')
        hemowork5_easy4.make_dir(dir_name)
    elif exitos == '0':
        pass
    else:
        print('Такого пункта нет в меню')