# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

num_n = int(input('Enter the number: '))

lst_nums = list(range(-abs(num_n), abs(num_n) + 1))

if num_n < 0:
    lst_nums.reverse()

number_els = 5

lst_i = []

for i in range(number_els):
    lst_i.append(int(input(f'Enter the {i+1} element: ')))

print()
print('Generated list:', lst_nums, sep='\n', end='\n\n')
print('Indexes for multiplication:', lst_i, sep='\n', end='\n\n')

result = 1

for indx in lst_i:
    result *= lst_nums[indx]

print(f'Result: {result}')