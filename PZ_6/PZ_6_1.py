# Вариант 15
# Дан список A размера N. 
# Вывести его элементы в следующем порядке: A1, AN, A2, AN-1, A3, AN-2, .... 

import random

n = int(input("Введите размер списка: "))
a = [ ]

for i in range(n):
    a.append(random.randint(0, 100))
4
print("Исходный список: ", a)

b = [ ]

for i in range(n // 2):
    b.append(a[i])
    
