N = int(input("Введите N: "))

temp = N
print("Цифры числа:")
while temp > 0:
    digit = temp % 10
    print(digit)
    temp //= 10