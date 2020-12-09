# Задание 1
class my_Date:
    """Класс Моя_дата"""
    date = '8-12-2020'
    def __init__(self, date):
        my_Date.date = date

    @classmethod
    def transform(cls):
        """Метод класса изменеия строки с датой на числовые значения дат."""
        final_date = []
        for item in cls.date.split('-'):
            final_date.append(int(item))
        return final_date

    @staticmethod
    def validate():
        """Статический метод проверки корректности ввода даты."""
        if my_Date.transform()[0] in range(1, 13):
            print("Month is OK")
        else:
            print("Month is wrong")
        if my_Date.transform()[1] in range(1, 32):
            print("Day is OK")
        else:
            print("Day is wrong")



date1 = my_Date('15-12-2222')
date1.validate()
print(my_Date.transform())


# Задание 2

class DivideException(Exception):
    def __init__(self, text):
        self.text = text

def division(x, y):
    """Функция деления"""
    if y == 0:
        raise DivideException('Делить на ноль нельзя!')
    else:
        return x / y

# print(division(10, 1))

# Задание 3

class OnlyIntsList(Exception):
    """Класс-исключение, который вызывается при вводе не числового значения пользователем"""
    def __init__(self, text):
        self.text = text


def AskingInts():
    """Функция, которая бесконечно запрашивает у пользователя числовые значения и добавляет их в финальный список"""
    IntsList = []
    while True:
        NextNum = input('Ввведите число. Чтобы прекратить цикл введите "Stop": ')
        if NextNum == 'Stop':
            break
        try:
            if not NextNum.isdigit():
                raise OnlyIntsList('Вы ввели не числовое значение, повторите попытку')
        except:
            print('Введено не числовое значение')
            continue
        IntsList.append(int(NextNum))
    print(IntsList)

AskingInts()

# Задание 4-6
class DataException(Exception):
    """Дочерний класс-исключение для проверки правильности вводимых данных в методах класса Склад"""
    def __init__(self, text):
        self.text = text

class Warehouse:
    """Класс Склад."""
    def __init__(self, area, height):
        self.area = area
        self.heigh = height
        self.W_size = area * height
        self.stack = []

    def acceptance(self, other):
        """Метод приема товара на склад."""
        self.stack.append({'name': other.name, 'quantity': other.quantity, 'size': other.size, 'sum_size': other.sum_size})
        self.W_size -= other.sum_size
        print(f'На склад загружены {other.quantity} единиц оргтехники {other.name} общим объемом {other.sum_size} м3. Свободного места на складе: {self.W_size} м3')

    def shipment(self, department_name, equip_name, equip_quant):
        """Метод отгрузки товара со склада в определенный отдел компании."""
        count = 0
        real = False
        try:
            if not isinstance(equip_quant, int):
                raise DataException('Введено неверное значение количества единиц техники')
            elif not isinstance(equip_name, str):
                raise DataException('Введено неверное значение названия товара')
            elif not isinstance(department_name, str):
                raise DataException('Введено неверное значение названия подразделения')
        except Exception as ex:
            print(ex)
            return
        for el in self.stack:
            if equip_name == el.get('name'):
                self.stack[count].update({'quantity': el.get('quantity') - equip_quant})
                self.stack[count].update({'sum_size': el.get('sum_size') - equip_quant * el.get('size')})
                self.W_size += equip_quant * el.get('size')
                real = True
            count += 1
        if real == True:
            print(f'В подразделение {department_name} были отгружены {equip_quant} единиц техники {equip_name}. Свободного места на складе: {self.W_size} м3')
        else:
            print(f'Такой техники на складе нет')

class Office_equip:
    """Родительский класс оргтехники."""
    def __init__(self, size, electricity, quantity):
        self.size = size
        self.electricity = electricity
        self.quantity = quantity
        self.sum_size = size * quantity

class Printer(Office_equip):
    """Дочерний класс оргтехники - Принтер."""
    def __init__(self, name, size, electricity, quantity, color):
        super().__init__(size, electricity, quantity)
        self.color = color
        self.name = 'Printer ' + name

class Scaner(Office_equip):
    """Дочерний класс оргтехники - Сканер."""
    def __init__(self, name, size, electricity, quantity, type):
        super().__init__(size, electricity, quantity)
        self.type = type
        self.name = 'Scaner ' + name

class Copier(Office_equip):
    """Дочерний класс оргтехники - Ксерокс."""
    def __init__(self, name, size, electricity, quantity, paper_formats):
        super().__init__(size, electricity, quantity)
        self.paper_formats = paper_formats
        self.name = 'Copier ' + name

firm_warehouse = Warehouse(500, 6)
printers = Printer('HP', 15, True, 10,  'black and white')
print(printers)
scaners = Scaner('Xerox', 10, True, 20, 'laser')
print(scaners.sum_size)
copiers = Copier('LG', 35, True, 45, ['A4', 'A3'])

print(firm_warehouse.W_size)
firm_warehouse.acceptance(printers)
firm_warehouse.acceptance(scaners)
firm_warehouse.acceptance(copiers)
print(firm_warehouse.W_size)
print(firm_warehouse.stack)
firm_warehouse.shipment('Sales dep', 'Copier LG', 30)
print(firm_warehouse.stack)
firm_warehouse.shipment('Head office', 'Scaner Xerox', 15)
print(firm_warehouse.stack)
firm_warehouse.shipment('Development dep', 'Printer HP', 7)
print(firm_warehouse.stack)
firm_warehouse.shipment('dfsfsdfs', 6, 7)
firm_warehouse.shipment(7, 'sdfsdf', 4)
firm_warehouse.shipment('sdfsd', 'dsdfsd', 'fsdfsd')

# Задание 7

class complex_ints:
    """Класс комплексное число."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def make_copmlex(self):
        """Метод отображения комплексного числа из двух переменных, заданных пользователем."""
        return self.x + self.y * 1j

    def __add__(self, other):
        """Перегруженные метод сложения комплексных чисел."""
        return self.x + other.x + self.y * 1j + other.y * 1j

    def __mul__(self, other):
        """Перегруженные метод умножения комплексных чисел."""
        return self.x * other.x + self.x * other.y * 1j + self.y * 1j * other.x + self.y * 1j * other.y * 1j

com1 = complex_ints(1, -3)
com2 = complex_ints(8, 3)
print(com1.make_copmlex())
print(com1 + com2)
print(com1 * com2)