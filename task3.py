def my_func(number1, number2, number3):
    my_list = [number1, number2, number3]
    total = []
    max1 = max(my_list)
    total.append(max1)
    my_list.remove(max1)
    max2 = max(my_list)
    total.append(max2)
    return sum(total)


print(my_func(number1=int(input('Введите первое число\n')),
              number2=int(input('Введите второе число\n')),
              number3=int(input('Введите третье число\n'))))

