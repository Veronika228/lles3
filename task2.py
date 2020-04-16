name = input('Введите имя\n')
surname = input('Введите фамилию\n')
birth_year = int(input('Введите год рождения\n'))
city = input('Введите город проживания\n')
email = input('Введите вашу почту\n')
phone_number = int(input('Введите ваш номер телефона\n'))


def my_func(name, surname, birth_year, city, email, phone_number):
    return f'{name} {surname} -- {birth_year}, {city} -- {email}, {phone_number}'


print(my_func(name, surname, birth_year, city, email, phone_number))