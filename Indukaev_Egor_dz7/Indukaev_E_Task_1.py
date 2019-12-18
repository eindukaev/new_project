#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в
# виде прямоугольной схемы. Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица. Подсказка: сложение элементов
# матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым
# элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, list_list):
        #self.list_list = [i for i in list_list]
        self.list_list = list_list

    def __str__(self):
        for self.str_list in self.list_list:
    #         return ('\n'.join(map(str, self.str_list)))
            return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.list_list]) + '\n'

    def __add__(self, other):
        res=[]
        a = len(self.list_list)
        b = len(self.list_list[0])
        #print(b)
        for raw in range(a):
            i_str = []

            for i in range(b):
                summa = self.list_list[raw][i] + other.list_list[raw][i]
                i_str.append(summa)
            res.append(i_str)
        return Matrix(res)


list_list = [[2, 1, 3], [8, 4, -1]]
matr1 = Matrix(list_list)
print(matr1)

list_list = [[1, 3, 6], [2, 4, 1]]
matr2 = Matrix(list_list)
print(matr2)

print(matr1 + matr2)