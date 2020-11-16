# определение типа элемента

my_list = [1, "sd", ('ar', 15), 1.5, ['ge', 77]]
def types(el_list):
	for el in el_list:
		print('element:', el, "-", type(el))
types(my_list)
print()

# обмен элементами

your_list = list(input('Введите элементы списка: '))
last = your_list[-1]
for ind, el in enumerate(your_list):
	if ind % 2 != 0:
		your_list[ind-1] = el
		your_list[ind] = temp
	temp = el
print(your_list)

# Времена года
# # Решение через list

list_seasons = ['Зима', 'Зима', "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
try:
	month_num = int(input("Введите номер месяца по порядку: "))-1
	n = list_seasons[month_num]
	print(f'Месяц относится ко времени года: {n}')
except Exception as e:
	print('Введены некорректные данные, попробуйте еще раз')

# # Решение через словарь

seasons_dict = {
	1: 'Зима',
	2: "Зима",
	3: "Весна",
	4: "Весна",
	5: "Весна",
	6: "Лето",
	7: "Лето",
	8: "Лето",
	9: "Осень",
	10: "Осень",
	11: "Осень",
	12: "Зима"
}
month_num = int(input("Введите номер месяца по порядку: "))
if month_num not in range(1, 13):
	print("Введено некорректное значение , попробуйте еще раз.")
else:
	print(f'Месяц относится ко времени года: {seasons_dict.get(month_num)}')

# Слова с новой строки

your_string = input("Введите строку: ").split(' ')
for num, word in enumerate(your_string, 1):
	print(num, word[:10])

# Рейтинг

my_rating = [38, 25, 16, 8, 8, 5, 2, 1, 1]
your_points = int(input('Введите количество очков рейтинга: '))
for el in my_rating:
	if your_points > el:
		my_rating.insert(my_rating.index(el), your_points)
		break
print(my_rating)

# Товары

cat = []

for b in range(1, 4):
	print(f"Товар {b}")
	cat.append(
		(b,
		 {"Название": input(f"Введите название товара {b}: "),
		  "Цена": input(f"Введите цену товара {b}: "),
		  "Количество": input(f"Введите колличество товара {b}: "),
		  "Ед": input(f"Введите единицы измерения товара {b}: ")}
	))

print(cat)

names = []
price = []
quantity = []
unit =[]

for b in cat:
	names.append(b[1].get("Название"))
	price.append(b[1].get("Цена"))
	quantity.append(b[1].get("Количество"))
	unit.append(b[1].get("Ед"))

if len(unit) > 1 and len(set(unit)) == 1:
	unit = list(set(unit))

analytics = {
	"Название": names,
	"Цена":price,
	"Количество":quantity,
	"Ед":unit
}

print(analytics)





