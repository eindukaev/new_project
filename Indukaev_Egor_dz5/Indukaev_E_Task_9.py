# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
import  json

with open('Task_7.txt', 'r') as file_l:
    #file_v = {i[0]: i for i in file_l.read().splitlines()}
    file_v = [i.split(' ') for i in file_l.read().splitlines()]
    #i[0] for i in file_v
    print(file_v)
file_l.close()
