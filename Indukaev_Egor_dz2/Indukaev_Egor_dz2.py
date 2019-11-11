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

#Task_3:
season = {'winter': (12, 1, 2), 'spring': (3, 4, 5),'summer': (6, 7, 8), 'autumn': (9, 10, 11)}
num_month = int(input('Введите номер месяца: '))
for i in season.keys():
    if num_month in season[i]:
        print(i)