import json


def check_el(data=None, data2=None):
    result = [x for x in data if x not in data2]
    print(f'Внесены изменения, смотри {result}')


with open('list.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    #print(data)

with open('list.json', 'r', encoding='utf-8') as file:
    data2 = json.load(file)
    #print(data2)

if len(data2) > len(data):
    print('Новый фаил больше, сравниваем элементы списка, узнаем какие элементы добавили')
    check_el(data2, data)
elif len(data2) == len(data):
    print('Файлы идентичны по рамеру(одинаковое количество эл массива), удалён или добавлен функционал')
    check_el(data2, data)
else:
    print('Старый фаил больше, сравниваем элементы списка, узнаем какие элементы удалены')
    check_el(data, data2)