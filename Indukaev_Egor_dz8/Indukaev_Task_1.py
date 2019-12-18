# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:

    @classmethod
    def date_converter(self, date):
        date_new = [int(i) for i in date.split('-')]
        return f' day: {date_new[0]} month: {date_new[1]} year: {date_new[2]}'

    @staticmethod
    def daet_validate(date):
        date_new = [int(i) for i in date.split('-')]
        if date_new[0] not in range(1, 32):
            return f' day: {date_new[0]} не корректный формат дня'
        elif date_new[1] not in range(1, 13):
            return f' month: {date_new[1]}  не корректный формат месяца'
        elif date_new[2] not in range(1900, 3000):
            return f' year: {date_new[3]}  не корректный формат года'
        else:
            return f' day: {date_new[0]} month: {date_new[1]} year: {date_new[2]}'


print(Date.date_converter('12-12-2019'))
print(Date.daet_validate('12-12-2019'))
