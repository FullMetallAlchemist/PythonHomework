# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def pari(list):
    list_num = []
    count = -1
    i = 0
    lenf = len(list) / 2
    while i < lenf:
        list_num.append(list[i]*list[count])
        count -= 1
        i += 1
    return list_num


list = [2, 3, 4, 5, 6]
list_num = pari(list)
print(list)
print(list_num)