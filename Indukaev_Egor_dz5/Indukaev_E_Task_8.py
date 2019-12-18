# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json


with open('Task_8.txt', 'r') as file_txt:
    line = [i.split(',') for i in (file_txt.read().splitlines())]
    average_profitDict = {i[0]: int(i[2]) - int(i[3]) for i in line if int(i[2]) > int(i[3])}
    average_damagesDict = {i[0]: int(i[2]) - int(i[3]) for i in line if int(i[2]) < int(i[3])}
    #print(average_profitDict)
    #print(average_damagesDict)
    #profit = [int(i[2]) - int(i[3]) for i in line if int(i[2]) > int(i[3])]
    #print(f'прибыль {profit}')
    #list_json =[dict(zip([i[0] for i in line], profit)), dict(average_profit = sum(profit) // len(profit))]
    list_json =[average_profitDict, dict(average_profit = sum(average_profitDict.values()) // len(average_profitDict)), average_damagesDict]
    with open('list.json', 'w') as fi_json:
        json.dump(list_json, fi_json)
        print(list_json)
        fi_json.close()
file_txt.close()
