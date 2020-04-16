# Первый вариант


def my_func(number1, number2):
    return number1 ** number2


number1 = int(input('Введите положительное число.\n'))
if number1 > 0:
    number2 = int(input('Введите целое отрицательное число.\n'))
    if not number2 < 0:
        print('Введено не правильно.\n')
        number2 = int(input('Введите целое отрицательное число.\n'))
else:
    print('Введено не правильно.\n')

print(my_func(number1, number2))

# Второй вариант


def my_func(number1, number2):
    return pow(number1, number2)


number1 = int(input('Введите положительное число.\n'))
if number1 > 0:
    number2 = int(input('Введите целое отрицательное число.\n'))
    if not number2 < 0:
        print('Введено не правильно.\n')
        number2 = int(input('Введите целое отрицательное число.\n'))
else:
    print('Введено не правильно.\n')

print(my_func(number1, number2))


# Третий вариант

number1 = int(input('Введите положительное число.\n'))
if number1 > 0:
    number2 = int(input('Введите целое отрицательное число.\n'))
    if not number2 < 0:
        print('Введено не правильно.\n')
        number2 = int(input('Введите целое отрицательное число.\n'))
else:
    print('Введено не правильно.\n')

b = abs(number2)
a = 1 / (pow(number1, b))
print(a)