# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input('Введите N: '))
arr = []
for i in range(n):
    arr.append(int(input('Введите элемент массива: ')))
x = int(input('Введите искомое число: '))

min_diff = x - arr[0]
if min_diff < 0:
    min_diff *= (-1)
res = arr[0]
for i in range(1, n):
    diff = x - arr[i]
    if diff < 0:
        diff *= (-1)
    if diff <= min_diff:
        min_diff = diff
        res = arr[i]
print(f'-> {res}')
