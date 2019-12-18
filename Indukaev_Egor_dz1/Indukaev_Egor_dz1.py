# Task_1.1
a = 1
print("a: ", a)
b = 'text'
print("b: ", b)
c = int(input("Введите целое чило: "))
print(f"c: {c}")
d = input("Введите текст: ")
print(f"c: {d}")

# Task_1.2
s = int(input("Введите время в сек: "))
hour = s // 3600
min = (s - hour * 3600) // 60
sec = s - hour * 3600 - min * 60
print(f'{hour}:{min}:{sec}')

# Task_1.3
n = str(input("Введите целое число: "))
nn = n + n
nnn = nn + n
num = int(n) + int(nn) + int(nnn)
print(f'{num}')

# Task_1.4
while True:
    n = int(input("Введите целое положительное число: "))
    if n > 0:
        while n > 10:
            n = list(f'{n}')
            print("Максимальное цифра введенного числа: ", max(n))
        print("Максимальное цифра: ", n)
        break
    else:
        print("Вы ввели не верное значение! Попробуйте ещё раз \n")

# Task_1.5
profit = int(input("Введите прибыль вашей фирмы: "))
cost = int(input("Введите издержки вашей фирмы: "))
if profit > cost:
    print("Ваша фирма в плюсе!")
    rev = profit - cost
    rent = (rev / profit) / 100
    print(f"Рентабельность вашей выручки составляет: {rent}")
    worker = int(input("Введите количество сотрудников: "))
    profit_worker = profit / worker
    print(f"Выручка одного работника составляет: {profit_worker}")
else:
    print("Ваша фирма в минусе")

# Task_1.6
a = int(input("Введите со скольки км хотите начать: "))
b = int(input("Введите результат которого хотите достигнуть: "))
day = 1

while a < b:
    #a = (a * 0.1) + a
    a *= 1.1
    day = day + 1

print(f"Через {day} days вы достигните реультата к которому стремитесь")