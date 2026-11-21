# Вариант 15
# Составить функцию, которая выведет на экран строку, 
# содержащую задаваемое с клавиатуры число символов

def line_print(n):
    line = " "
    for i in range(n):
        line += symbol
    return line

n = input("Введите число символов: ")
symbol = input("Введите символ: ")

while type(n) != int:  # обработка исключений 
    try: 
        n = int(n) 
    except ValueError: 
        print("Неправильно ввели!") 
        n = input("Введите целое число: ") 

print("Полученная строка: ", line_print(n))
       
    