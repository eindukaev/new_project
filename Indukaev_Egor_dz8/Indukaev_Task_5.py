# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение
# компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.


class Repository:
    def __init__(self):
        print(f'«Склад оргтехники»')

class Orgs:
    def __init__(self, type_org='', model='', id_org=None):
        self.count = []
        self.type_org = type_org
        self.model = model
        self.id_org = id_org

    @staticmethod
    def accept(**kwargs):
        list_el = [kwargs]
        print(list_el)


class Printer(Orgs):
    def __init__(self, type_org='', model='', id_org=None, type_p=''):
        super().__init__(type_org, model, id_org)
        self.type_p = type_p

class Scan(Orgs):
    def __init__(self, type_org='', model='', id_org=None, save_device=''):
        super().__init__(type_org, model, id_org)
        self.save_device = save_device

class Xerox(Orgs):
    def __init__(self, type_org='', model='', id_org=None, num_of_copy=None):
        super().__init__(type_org, model, id_org)
        self.count_copy = num_of_copy

Repository()
tp = Printer(type_p='Лазерный')
print(tp.type_p)

Orgs.accept(type_org='Printer', model='Hp', id_org=1)