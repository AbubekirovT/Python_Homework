# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2


number = int(input('Введите количество монет: '))
head = 0
tail = 0
for _ in range(number):
    coin = int(input('Введите положение монеты(0 или 1): '))
    if coin == 0: tail += 1
    else: head += 1

if head < tail: print(head)
else: print(tail)