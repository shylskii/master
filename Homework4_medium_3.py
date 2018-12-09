import random

random_list = [random.randint(1, 5) for i in range(2500)]

str_random_list = ''.join([str(x) for x in random_list])

print(str_random_list)

print(len(str_random_list))

with open('random_string.txt', 'w') as r:
    r.write(str_random_list)
counter = ''
sorted_and_grouped = []

for i in range(len(str_random_list)-1):
    if str_random_list[i] == str_random_list[i+1]:
        counter += str(str_random_list[i])
    else:
        counter += str(str_random_list[i])
        sorted_and_grouped.append(counter)
        counter = ''

list_lengthes = (list(map(len, sorted_and_grouped)))
print(f'длина= {len(list_lengthes)} == длина отсортированных и сгрупированных= {len(sorted_and_grouped)}')

max_number_of_repeats = max(list_lengthes)
print(f'Максимальное число повторений= {max_number_of_repeats}')

index_of_max_repeats = list_lengthes.index(max_number_of_repeats)
biggest_number = sorted_and_grouped[index_of_max_repeats]
print(f'Наибольшая последовательность= {biggest_number}')