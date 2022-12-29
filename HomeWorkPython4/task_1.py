# 1. Пользователь вводит число, Вам необходимо вывести число Пи с
# той точностью знаков после запятой, сколько указал пользователь(БЕЗ round())

from math import pi

number_of_places = int(input("Enter the number of decimal places you want to see: "))
degree = 10**number_of_places 
s = float(int(pi*degree)/degree)
print (s)
print (pi)