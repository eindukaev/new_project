# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def info(name, surname, year, city, email, phone):
    return f'Данные о пользователе: \n имя: {name}, фамилия: {surname}, год рождения: {year}, город проживания: {city}, email: {email}, телефон: {phone}'


# user_date = (input('Введите данные пользователя в формате: имя, фамилия, год рождения, город проживания, email, телефон: '))
# user_date = user_date.split(','' ')
# for i in user_date:
#     user_date[i]
name = input('input name: ')
surname = input('input surname: ')
year = input('input year of birth: ')
city = input('input city of residence: ')
email = input('input email: ')
phone = input('input phone: ')

print(info(name=name, surname=surname, year=year, city=city, email=email, phone=phone))
