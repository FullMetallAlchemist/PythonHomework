# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

def factorial(n):
    count = 1
    for i in range (1, n + 1):
        count*=i
        print(count, end = ", ")

n = int(input('Введите число N: '))
factorial(n)