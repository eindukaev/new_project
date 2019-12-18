# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_funk(a, b, c):
    my_list = [a, b, c]  # элементы to список
    my_list.sort(reverse = True)
    sum_l = my_list[0] + my_list[1]
    return sum_l

    # max_unit = max(my_list)  # вычисляем макс значение и заносим в
    # my_list.pop(my_list.index(max_unit))
    # max_unit_2 = max(my_list)
    #return max_unit + max_unit_2  # возвращает сумму наибольших двух аргументов

while True:
    a = input('Введите первое значение: ')
    b = input('Введите второе значение: ')
    c = input('Введите третье значение: ')
    if a.isdigit() & b.isdigit() & c.isdigit():
        print(my_funk(int(a), int(b), int(c)))
        break
    else:
        print('Вы ввели некоректные значениея! Попробуйте ещё раз!')
