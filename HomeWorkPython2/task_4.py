# 4)Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

a = 1
num_n = int(input("b = "))
sum_numbers = 0
for i in range(a, num_n + 1):
    if i % 2 == 0:
        sum_numbers += i
print(sum_numbers)