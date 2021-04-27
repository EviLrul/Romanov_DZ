# Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведённых типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают
# за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
#
# Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
import sys


class EquipmentWarehouse:
    def __init__(self, name):
        self.equipment = {}
        self.all_info = []
        self.name = name

    def __str__(self):
        out_str = f'Наименование склада: {self.name}\n'
        if not self.all_info:
            out_str = out_str + 'Склад пуст' + '\n'
        else:
            for i in range(len(self.all_info)):
                out_str = out_str + str(self.all_info[i]) + '\n'
            out_str = out_str + '\nВсего: ' + str(self.equipment) + '\n'
        return out_str

    def add_equipment(self, obj):
        self.all_info.append(dict([('Техника', obj.type_equipment), ('Наименование', obj.name_equipment),
                                   ('Серийный №', obj.s_n)]))
        if obj.type_equipment in self.equipment:
            self.equipment[obj.type_equipment] = self.equipment[obj.type_equipment] + 1
        else:
            self.equipment[obj.type_equipment] = 1

    def moving_equipment(self, obj, where_to_location):
        temp_all_info = []
        for i in range(len(self.all_info)):
            if self.all_info[i]['Серийный №'] != obj.s_n:
                temp_all_info.append(self.all_info[i])
        self.all_info = temp_all_info
        self.equipment[obj.type_equipment] = self.equipment[obj.type_equipment] - 1
        if self.equipment[obj.type_equipment] == 0:
            self.equipment.pop(obj.type_equipment)
        where_to_location.add_equipment(obj)


class Equipment:
    def __init__(self, type_equipment):
        self.type_equipment = type_equipment


class Equipment_Printer(Equipment):
    def __init__(self, type_equipment, name_printer, s_n):
        super().__init__(type_equipment)
        self.name_equipment = name_printer
        self.s_n = s_n


class Equipment_Scan(Equipment):
    def __init__(self, type_equipment, name_scan, s_n):
        super().__init__(type_equipment)
        self.name_equipment = name_scan
        self.s_n = s_n


class Equipment_Xerox(Equipment):
    def __init__(self, type_equipment, name_xerox, s_n):
        super().__init__(type_equipment)
        self.name_equipment = name_xerox
        self.s_n = s_n


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    equipment = input('Введите модель принтера:')
    if equipment.isdigit():
        raise OwnError("Вы ввели не модель, а число!")
    equipment_s_n = input('Введите инвентарный номер принтера:')
    if not equipment_s_n.isdigit():
        raise OwnError("Инвентарный номер должен состоять из цифр")
except OwnError as err:
    print(err)
    sys.exit()

printer_1 = Equipment_Printer('Принтер', equipment, int(equipment_s_n))
printer_2 = Equipment_Printer('Принтер', 'Samsung ML-1210', 8797798)
scan_1 = Equipment_Scan('Сканер', 'Canon Lide-210', 12313)
scan_2 = Equipment_Scan('Сканер', 'Canon Lide-210', 78978)
xerox_1 = Equipment_Xerox('Копир', 'Sharp 6020', 54646)
sklad_1 = EquipmentWarehouse('Склад техники')
sklad_2 = EquipmentWarehouse('Малый офис')
sklad_3 = EquipmentWarehouse('Старший офис')
sklad_1.add_equipment(printer_1)
sklad_1.add_equipment(printer_2)
sklad_1.add_equipment(scan_1)
sklad_1.add_equipment(xerox_1)
sklad_1.add_equipment(scan_2)
print('Заполнение складов -------------------------------')
print(sklad_1)
print(sklad_2)
print(sklad_3)
sklad_1.moving_equipment(printer_1, sklad_2)
sklad_1.moving_equipment(scan_1, sklad_3)
print('Перемещение по складам 1 -----------------------------')
print(sklad_1)
print(sklad_2)
print(sklad_3)
sklad_2.moving_equipment(printer_1, sklad_3)
print('Перемещение по складам 2 -----------------------------')
print(sklad_1)
print(sklad_2)
print(sklad_3)
sklad_1.moving_equipment(xerox_1, sklad_2)
print('Перемещение по складам 3 -----------------------------')
print(sklad_1)
print(sklad_2)
print(sklad_3)
