# Вариант 15
# Дано вещественное число A и целое число N (>0). 
# Используя один цикл, найти сумму 1 + A + A^2 + A^3 + ... + A^N.

A = input("Введите вещественное число A: ")
N = input("Введите целое число N (>0): ")

while type(A) != float: # обработка исключений
    try:
        A = float(A)
    except ValueError:
        print("Неправильно ввели!")
        A = input("Введите вещественное число: ")

while type(N) != int: # обработка исключений
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите целое число: ")

while True:
    if N <= 0:
        print("Ошибка!")
        N = int(input("Введите целое число N (>0): "))
    else:
        break

k = 0
summa = 1
num = 1

while k != N:
    num = num * A
    summa = summa + num
    k = k + 1
print("Сумма равна:", summa)