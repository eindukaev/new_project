# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к
# клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
# соответственно. В методе деления должно осуществляться округление значения до целого числа.
# Сложение.
# Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме
# ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количестваячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество
# ячеек в ряду. Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку
# вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек
# на формирование ряда не хватает, то в последний ряд записываются все оставшиеся. Например,
# количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку: *****\n*****\n**. Или, количество ячеек клетки равняется 15, количество ячеек
# в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
class Cell:
    def __init__(self, integer):
        self.integer = integer
        #self.n = 0

    def __str__(self):
        return str(self.integer)

    def __add__(self, other):
        return Cell(self.integer + other.integer)

    def __sub__(self, other):
        if self.integer > other.integer:
            return Cell(self.integer - other.integer)
        else:
            return f'''  Разность количества ячеек двух клеток меньше нуля. 
    Переопределите количество ячеек для первой клетки'''

    def __mul__(self, other):
        return Cell(self.integer * other.integer)

    def __truediv__(self, other):
        return Cell(self.integer // other.integer)

    def make_order(self, n):
        #return ' '.join([str(i) for i in range(1, self.integer + 1)])
        str_cell = ' '.join(['%d' % i for i in range(1, self.integer+1)])
        #print(str_cell[1])
        #str_cell = [i for i in range(1, self.integer + 1)]
        #print(self.integer)
        index_el = [n * i - 1 for i in range(1, (len(str_cell) - 1) // n)]
        #index_el = [n * i for i in range(1, (self.integer // n)+1)]
        #print(str_cell[0])
        print(index_el)
        for el in index_el:
            if str_cell[el] in str_cell:
                str_cell[el] = '\n'
                return
                #return str_cell.replace(str_cell[el], '\n')
        #return [str_cell.replace(str_cell[el], '\n') for el in index_el if str_cell[el] in str_cell]


cell_one = Cell(10)
cell_two = Cell(20)
print(f'Сумма ячеек: \n  {cell_one + cell_two}')
print(f'Разность ячеек: \n  {cell_one - cell_two}')
print(f'Произведение ячеек: \n  {cell_one * cell_two}')
print(f'Деление ячеек: \n  {cell_one / cell_two}')
#print(f' {cell_one.make_order(4)}')
print(cell_one.make_order(4))
#cell_two.make_order(5)
#print(f'{}')

