# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8


number = int(input('Введите натуральное число: '))
n = 1
while n<=number:
    print(n, end=' ')
    n *= 2