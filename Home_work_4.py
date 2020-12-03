def count_salary():
	"""Функция расчета зарплаты"""
	try:
		pay_per_hour = int(input("Введите ставку работника в час: "))
	except:
		print("Ввведены некорректные данные, попробуйте еще раз")
		return
	try:
		workers_hours = int(input("Введите выработку работника в часах: "))
	except:
		print("Ввведены некорректные данные, попробуйте еще раз")
		return
	try:
		workers_prize = int(input('Введите премию работника: '))
	except:
		print("Ввведены некорректные данные, попробуйте еще раз")
		return
	final_result = pay_per_hour * workers_hours + workers_prize
	print(final_result)

count_salary()

def next_numb_bigger():
	"""Последовательность чисел, в которых следующий элемент больше"""
	try:
		numb_input = input("Введите последовательность чисел через пробел: ")
		final_numb_list = []
		numb_list = enumerate(numb_input.split(' '))
		last = 0
		for index, numb in numb_list:
			if int(numb) > last:
				final_numb_list.append(numb)
			last = int(numb)
	except Exception as error:
		print("Ввведены некорректные данные, попробуйте еще раз")
		return
	print(final_numb_list)

next_numb_bigger()

# Генератор чисел кратных 20 и 21

generate_2021 = [el for el in range(20, 241) if el % 20 ==0 or el % 21 == 0]
print(generate_2021)

# Генератор списка с уникальными элементами

new_numbs_list = input("Введите последовательность чисел через пробел: ")
new_numbs_list_final = new_numbs_list.split(' ')
try:
	for elem in new_numbs_list.split(' '):
		elem = int(elem)
	generate_uniq = [el for el in new_numbs_list_final if new_numbs_list_final.count(el) == 1]
	print(generate_uniq)
except:
	print("Ввведены некорректные данные, попробуйте еще раз")

# Формирование списка  и умножение всех элементов при помощи reduce() 

from functools import reduce

generate_100_1000 = (el for el in range(100, 1001))
final_result = reduce(lambda el1, el2: el1 * el2, generate_100_1000)
print(final_result)

# Итераторы

def iterator_range():
	"""Итератор, который генерирует целые числа в указанном диапазоне"""
	try:
		first_num = int(input("Введите число, с которого начнется генерация новых целых чисел: "))
		last_num = int(input('Введите число, на котором цикл должен прекратиться: '))
		generate_range = [el for el in range(first_num, (last_num+1))]
		yield generate_range
	except:
		print("Ввведены некорректные данные, попробуйте еще раз")

for items in iterator_range():
	print(items)

def iterator_repeat(example_list):
	"""Итератор повторяющий элементы списка"""
	from itertools import cycle
	count = 0
	for item in cycle(example_list):
		if count > 40:
			break
		print(item)
		count += 1

iterator_repeat(generate_2021)


def fact(n):
	"""Функция с генератором факториалов"""
	from math import factorial
	my_generator = (factorial(el) for el in range(1, n))
	for elem in my_generator:
		yield elem

for el in fact(10):
	print(el)

