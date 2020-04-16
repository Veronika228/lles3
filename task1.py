number1 = int(input('введите первое число'))
number2 = int(input('введите второе число'))


def my_func(number1: int, number2: int):
    return number1 / number2


if ZeroDivisionError:
    print('Деление не возможно')
    number1 = int(input('введите первое число'))
    number2 = int(input('введите второе число'))

print(my_func(number1, number2))