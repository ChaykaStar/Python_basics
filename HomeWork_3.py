# Функция деления

def divide(x, y):
	if y == 0:
		return "Делить на ноль нельзя"
	else:
		return x / y

print(divide(1, 5))

# Функция анкета

def form(name="Никита", surname="Чайка", birth_date="1991", email="chaykastar@gmail.com", phone='89999999999'):
	return f'Имя : {name}, Фамилия: {surname}, Год рождения: {birth_date}, Е-мейл: {email}, Номер телефона: {phone}'

print(form())

# Функция my_func()

def my_func(x, y, z):
	lis = [x, y, z]
	return max(lis)

print(my_func(1, 5, 18))

# Функция возведения в отрицательную степень

def exponent(x, y):
	if x > 0 and x % 1 == 0 and y < 0 and y % 1 == 0:
		pass
	else:
		return 'Введены некорректные данные'
	x_1 = x
	for b in range(1, abs(y)):
		x *= x_1
	return 1 / x

print(exponent(2, -3))

# Функция с запрсоом данных у клиента

def inputs():
	summ = 0
	while True:
		numbers = input("Введите числа, которые нужно просуммировать через пробел:")
		for b in numbers.split():
			try:
				summ += int(b)
			except:
				return summ
				break
		print(summ)

print(inputs())

# Функция int_func()

def int_func(x):
	return x.title()

print(int_func('title'))

def int_func_input():
	string = input("Введите строку из слов латинскими буквами в нижнем регистре: ")
	final_string = ''
	for b in string.split():
		if final_string == '':
			final_string += int_func(b)
		else:
			final_string += ' ' + int_func(b)
	return final_string

print(int_func_input())
