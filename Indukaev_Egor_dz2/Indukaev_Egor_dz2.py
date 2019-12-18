# Task_1:
result_list = [True, 152, 'el', 'text', False, 'Text']

for i in result_list:
    print(type(i))

# Task_2:
inp_str = input('Введите элементы списка через пробел: ')
res_list = inp_str.split()

j = 0
for i in range(int(len(res_list)/2)):
   res_list[j], res_list[j+1] = res_list[j+1], res_list[j]
   j += 2
print(res_list)

# Task_3:
season = {'winter': (12, 1, 2), 'spring': (3, 4, 5),'summer': (6, 7, 8), 'autumn': (9, 10, 11)}
while True:
    try:
        num_month = int(input('Введите номер месяца: '))
        for i in season.keys():
            if num_month in season[i]:
                print(i)
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")

# Task_4
inp_str = input("Введите строку из нескольких слов, разделённых пробелами: ")
out_list = inp_str.split()
num = 0
for i in out_list:
    num += 1
    print(f"{num}) {i[0:10]}")

#Task_5
my_list = [7, 5, 3, 3, 2]
print('набор натуральных чисел рейтинга: 7, 5, 3, 3, 2')
while len(my_list) < 10:
    while True:
        try:
            el = int(input('Введите новое значение рейтинга: '))
            my_list.append(el)
            #print(my_list)
            my_list.sort(reverse = True)
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")
out_list = [str(x) for x in my_list]
print(', '.join(out_list))