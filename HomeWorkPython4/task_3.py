# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

def get_list_unique(lst: list):

    lst_unique = [el for el in lst if lst.count(el) == 1]

    return lst_unique

number_els = int(input('Enter the number of elements: '))

max_number = int(input('Enter the max number: '))

lst_in = [randint(0, max_number) for _ in range(number_els)]

print('Full list:', lst_in, sep='\n')

print('Unique elements:', *get_list_unique(lst_in))