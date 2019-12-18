
def f_del(a, b):
    return a / b


while True:
    try:
        a = int(input('Введите первое значение, a: '))
        b = int(input('Введите второе значение, b: '))
        if b != 0:
            print(f'результат от деления a на b: {f_del(a, b)}')
        else:
            print("На ноль деление запрещено, попробуйте ввести значение ещё раз!")
    except ValueError:
        print("Вы ввели не числовые значение, попробуйте снова!")
