# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
# title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из
# классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        #self.title = 'ручка'
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def draw(self):
        self.title = 'карандаш'
        print(f'Запуск отрисовки {self.title}ом')


class Handle(Stationery):
    def draw(self):
        self.title = 'маркер'
        print(f'Запуск отрисовки {self.title}ом')


instance_1 = Pen()
instance_1.title = 'ручка'
instance_1.draw()
print(instance_1.title)
instance_2 = Pencil()
instance_2.draw()
print(instance_2.title)
instance_3 = Handle()
instance_3.draw()
print(instance_3.title)

