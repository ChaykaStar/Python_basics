class TrafficLight:
	"""TrafficLight switches color for certain time."""
	import time
	__color = ['red', 'yellow', 'green']

	def running(self):
		while True:
			print(self.__color[0])
			self.time.sleep(7)
			print(self.__color[1])
			self.time.sleep(2)
			print(self.__color[2])
			self.time.sleep(7)


light = TrafficLight()
light.running()

class road:
	"""Class 'road' has method to calculate mass of materials need to pave the road."""
	def __init__(self, lenght, width):
		self._lenght = lenght
		self._width = width

	def mass_calculation(self, height):
		self.height = height
		self.mass_for_sq = 25
		return self._lenght * self._width * self.height * self.mass_for_sq

b = road(140, 10)
print(b.mass_calculation(7))

class Worker:
	"""Class 'Worker' initialize a worker"""
	def __init__(self, name, surname, position, wage, bonus):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
	"""Class 'Position' has two methods which can show us total income or full name of a worker"""
	def get_full_name(self):
		print(f'Полное имя сотрудника: {self.name} {self.surname}')

	def get_total_income(self):
		print(f'Общий доход сотрудника составляет: {self._income.get("wage") + self._income.get("bonus")}')


worker1 = Position("Андрей", "Малахов", "Говорун", 300, 100)
worker1.get_full_name()
worker1.get_total_income()

worker2 = Position('Никита', "Чайка", "SeniorEngineer", 10000000, 90000000)
worker2.get_full_name()
worker2.get_total_income()

worker3 = Position("Альберт", "Эйнштейн", "Гений", 99999999, 99999999)
worker3.get_full_name()
worker3.get_total_income()

class car:
	"""Basic class 'car' has methods to show characteristics of a car."""
	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		print("Машина поехала")

	def stop(self):
		print("Машина остановилась")

	def turn(self, direction):
		self.direction = direction
		print(f'Машина повернула {direction}')

	def showspeed(self):
		print(f'Скорость машины: {self.speed}')

	def showchar(self):
		if self.is_police == True:
			police_check = "является"
		else:
			police_check = "не является"
		print(f'Цвет машины: {self.color}\nНазвание машины: {self.name}\nМашина {police_check} полицейской')

class TownCar(car):
	"""Child class 'TownCar' of the class 'car'."""
	def __init__(self):
		super().__init__(speed = 60, color = 'white', name = 'towncar', is_police = False)

	def showspeed(self):
		if self.speed > 60:
			print(f'Превышение ограничения скорости 60! Скорость машины: {self.speed}')
		else:
			print(f'Скорость машины: {self.speed}')

class SportCar(car):
	"""Child class 'SportCar' of the class 'car'."""
	def __init__(self):
		super().__init__(100, 'red', 'SportCar', False)

class WorkCar(car):
	"""Child class 'WorkCar' of the class 'car'."""
	def __init__(self):
		super().__init__(50, 'gray', 'WorkCar', False)

	def showspeed(self):
		if self.speed > 40:
			print(f'Превышение ограничения скорости 40! Скорость машины: {self.speed}')
		else:
			print(f'Скорость машины: {self.speed}')

class PoliceCar(car):
	"""Child class 'PoliceCar' of the class 'car'."""
	def __init__(self):
		super().__init__(100, 'black and white', 'PoliceCar', True)


car1 = SportCar()
car1.showchar()
car1.turn("налево")
car1.stop()
car1.showspeed()
car1.go()

car2 = TownCar()
car2.showchar()
car2.turn("назад")
car2.stop()
car2.go()
car1.showspeed()

car3 = PoliceCar()
car3.showchar()
car3.turn("направо")
car3.stop()
car3.go()
car3.showspeed()

car4 = WorkCar()
car4.showchar()
car4.turn("вверх")
car4.stop()
car4.go()
car4.showspeed()


class Stationery:
	"""Basic class 'Stationery'."""
	def __init__(self, title):
		self.title = title
	def draw(self):
		print('Запуск отрисовки')

class Pen(Stationery):
	"""Child class 'Pen' of the class 'Stationery'."""
	def __init__(self):
		super().__init__('pen')
	def draw(self):
		print('Запуск отрисовки ручкой')

class Pencil(Stationery):
	"""Child class 'Pencil' of the class 'Stationery'."""
	def __init__(self):
		super().__init__('pencil')
	def draw(self):
		print('Запуск отрисовки карандашом')

class Handle(Stationery):
	"""Child class 'Handle' of the class 'Stationery'."""
	def __init__(self):
		super().__init__('handle')
	def draw(self):
		print('Запуск отрисовки маркером')

stat1 = Pen()
stat1.draw()

stat2 = Pencil()
stat2.draw()

stat3 = Handle()
stat3.draw()