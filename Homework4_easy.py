lst_1 = [2, 4, 6, 8, 10, 0, 3, 5]
print('lst_1:', lst_1)
lst_2 = list(map(lambda x: x**2, lst_1))
print('lst_2:', lst_2)

lst_fr_1 = ['Яблоко', 'Груша', 'Дыня', 'Лефрут', 'Маракуйа']
lst_fr_2 = ['Дыня', 'Грейпфрут', 'Апельсин', 'Персик', 'Лемон', 'Лефрут']
result = [_ for _ in lst_fr_1 if _ in lst_fr_2]
print(result)

lst_1_nums = [7, -8, 64, -5, -17, 24, 11, 12, 91, 122, -34, 204, 198, 210]
lst_2_nums = [i for i in lst_1_nums if  i >= 0 and i%4 and not i%3]
print(lst_2_nums)