# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).


class Worker:

    def __init__(self, name='', surname='', position='', **income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учётом премии равен {sum(self._income.values())}')


per_1 = Position(name='ivan', surname='Ivanov', position='clerc', wage= 150, bonus= 300)
print(per_1.name, per_1.surname, per_1.position, per_1._income)
per_1.get_full_name()
per_1.get_total_income()
