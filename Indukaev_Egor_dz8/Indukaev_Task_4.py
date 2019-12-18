# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники


class Repository:
    def __init__(self):
        print(f'«Склад оргтехники»')

class Orgs:
    def __init__(self, type_orgs='', model='', id_org=None):
        self.count = []
        self.type_org = type_orgs
        self.model = model
        self.id_org = id_org

class Printer(Orgs):
    def __init__(self, type_orgs='', model='', id_org=None, type_p=''):
        super().__init__(type_orgs, model, id_org)
        self.type_p = type_p

class Scan(Orgs):
    def __init__(self, type_orgs='', model='', id_org=None, save_device=''):
        super().__init__(type_orgs, model, id_org)
        self.save_device = save_device

class Xerox(Orgs):
    def __init__(self, type_orgs='', model='', id_org=None, num_of_copy=None):
        super().__init__(type_orgs, model, id_org)
        self.count_copy = num_of_copy

Repository()
tp = Printer(type_p='Лазерный')
print(tp.type_p)
