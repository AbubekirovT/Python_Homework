# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

s = int(input('Введите количество журавликов: '))
# s = x + x + 2(x + x) = 6x
if s%6 != 0:
    print('Некорректно задано число')

x = s//6
print(f'Петя и Сережа сделали {x} журавликов, а Катя {4*x}')