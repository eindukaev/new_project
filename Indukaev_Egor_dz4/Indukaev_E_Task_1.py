from sys import argv

argv_list = [int(i) for i in argv[1:]]
print('Ваша зарплата: ', (argv_list[0] * argv_list[1]) + argv_list[2])