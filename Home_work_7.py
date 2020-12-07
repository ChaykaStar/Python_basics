# Задание 1

class Matrix:
	"""Класс данных матрица дает возможность отображать матрицу 3х3 в привычном виде и суммировать матрицы формата 3х3"""
	def __init__(self, matrix):
		self.matrix = matrix

	def __str__(self):
		"""Отображает матрицу в привычном виде"""
		return f'''{self.matrix[0][0]} {self.matrix[0][1]} {self.matrix[0][2]}
{self.matrix[1][0]} {self.matrix[1][1]} {self.matrix[1][2]}
{self.matrix[2][0]} {self.matrix[2][1]} {self.matrix[2][2]}'''
	
	def __add__(self, other):
		"""Производит суммирование матриц"""
		return f'''{self.matrix[0][0] + other.matrix[0][0]} {self.matrix[0][1] + other.matrix[0][1]} {self.matrix[0][2] + other.matrix[0][2]}
{self.matrix[1][0] + other.matrix[1][0]} {self.matrix[1][1] + other.matrix[1][1]} {self.matrix[1][2] + other.matrix[1][2]}
{self.matrix[2][0] + other.matrix[2][0]} {self.matrix[2][1] + other.matrix[2][1]} {self.matrix[2][2] + other.matrix[2][2]}'''


mat1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat1)

mat2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(mat2)
print(mat1 + mat2)

# Задание 2

from abc import ABC, abstractmethod

class Wear(ABC):
	"""Класс одежда"""
	total = []
	def __init__(self, name, size):
		"""Конструктор класса Wear. Имеет атрибут, который суммирует расходы материала всех элементов класса"""
		self.name = name
		self.size = size
		self.used_textile = 0
		Wear.total.append(self.tis_cons)

	@abstractmethod
	def tis_cons(self):
		pass


class Coat(Wear):
	"""Дочерний класс класса одежда - пальто. Имеет метод расчета расхода материала для производста"""
	total = None
	def __str__(self):
		return f'Для пошива пальто {self.name} на размер {self.size} необходимо {self.size / 6.5 + 0.5} м2 ткани'

	@property
	def tis_cons(self):
		return self.size / 6.5 + 0.5


class Costume(Wear):
	"""Дочерний класс класса одежда - костюм. Имеет метод расчета расхода материала для производста"""
	total = None
	def __str__(self):
		return f'Для пошива костюма {self.name} на рост {self.size} необходимо {self.size * 2 + 0.3} м2 ткани'
	
	@property
	def tis_cons(self):
		return self.size * 2 + 0.3

costume = Costume('breeze', 2)
print(costume)
print(costume.tis_cons)

coat = Coat('imagine', 45)
print(coat)
print(coat.tis_cons)

print(sum(Wear.total))

# Задание 3

class Cell:
	def __init__(self, nucleus_num):
		self.nucleus_num = nucleus_num

	def __add__(self, other):
		return self.nucleus_num + other.nucleus_num

	def __sub__(self, other):
		if self.nucleus_num > other.nucleus_num:
			return self.nucleus_num - other.nucleus_num
		else:
			print('Разница количества ячеек клеток меньше нуля, произвести вычитание невозможно')

	def __mul__(self, other):
		return self.nucleus_num * other.nucleus_num

	def __truediv__ (self, other):
		return self.nucleus_num // other.nucleus_num

	def make_order(self, row_len):
		self.row_len = row_len
		if self.nucleus_num % self.row_len == 0:
			return ('*' * self.row_len + '\n') * (self.nucleus_num // self.row_len - 1) + '*' * self.row_len
		else:
			return ('*' * self.row_len + '\n') * (self.nucleus_num // self.row_len) + '*' * (self.nucleus_num % self.row_len)

cell1 = Cell(5)
cell2 = Cell(7)
cell3 = Cell(15)
print(cell3 * cell1)
print(cell3.make_order(3))
print(cell1 + cell2)
print(cell3 / cell2)
print(cell2 - cell3)
