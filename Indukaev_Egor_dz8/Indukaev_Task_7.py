# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComNumbers:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __add__(self, other):
        print(f'Сумма комплексных чисел: {complex(self.arg1, self.arg2) + complex(other.arg1, other.arg2)}')

    def __mul__(self, other):
        print(f'Произведение комплексных чисел: {complex(self.arg1, self.arg2) * complex(other.arg1, other.arg2)}')


num1 = ComNumbers(1, 2)
#print(num1)
num2 = ComNumbers(2, 4)
#print(num2)
num1 + num2
num1 * num2
#print(num1 + num2)