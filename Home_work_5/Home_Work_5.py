# Построчный ввод данных

with open('input_file.txt', 'a', encoding = 'UTF-8') as text_file:
	text_file.write(f'(\n{input("Введите данные первой строки: ")})')
	while True:
		text_string = input("Введите данные следующей строки: ")
		text_file.write(f'(\n{text_string})')
		if text_string == '':
			break

# Подсчет строк и символов в файле

with open('input_file.txt', 'r', encoding = 'UTF-8') as strings:
	strings_num = 0
	strings_len = ''
	for line in strings:
		print(line)
		strings_num += 1
		symbls = 0
		for symb in line:
			symbls += 1
		strings_len += (f'Строка {strings_num} - {symbls} символов\n')
print(f'Всего строк в файле: {strings_num}\nКоличество символов в строках: \n{strings_len}')

# Сотрудники с ЗП ниже 20 тыс

with open('workers.txt', 'r', encoding = 'UTF-8') as salaries:
	workers_loosers = ''
	workers_salaries_sum = 0
	workers_number = 0
	for worker in salaries:
		workers_salaries_sum += float(worker.split(' ')[1].replace('\n', ''))
		if float(worker.split(' ')[1].replace('\n', '')) < 20000:
			worker_looser = worker.split(' ')[0]
			workers_loosers += ' ' + worker_looser
		workers_number += 1
	average_salary =  workers_salaries_sum/workers_number
print(f'Сотрудники с зарплатой меньше 20000:{workers_loosers}')
print(f'Средняя зарплата: {average_salary}')


numbers = {'One': "Один", 'Two': "Два", 'Three': "Три", 'Four': "Четыре"}
def translater(file_name):
	"""Функция перевода числительных с английского на русский"""
	with open(file_name, 'r', encoding = 'UTF-8') as file:
		new_file = ''
		for string in file:
			new_file += (numbers.get(string.split(' — ')[0]) + ' — ' + string.split(' — ')[1])
		print(new_file)
		with open(('new_' + file_name), 'w', encoding='UTF-8') as file_new:
			file_new.write(new_file)

translater('one_two.txt')

def sumnumbers():
	"""Функция создает файл, записывает в него последовательность 
	чисел и суммирует их, затем выводит на экран сумму"""
	with open('summ.txt', 'w', encoding = 'UTF-8') as sumfile:
		try:
			numbers = input("Введите последовательность чисел через пробел: ")
			for num in numbers.split(' '):
				num = int(num)
		except:
			print("Введены неверные данные. попрoбуйте еще раз")
			return
		sumfile.write(numbers)
	with open('summ.txt', 'r', encoding = 'UTF-8') as sumfile_read:
		final_num = 0
		read = sumfile_read.read()
		for nums in read.split(' '):
			final_num += int(nums)
	print(final_num)

sumnumbers()

# Учебная программа

with open('subjects.txt', 'r', encoding = 'UTF-8') as encod:
	for subj in encod:
		sub_dict = {}
		name_sub = subj.split('   ')[0].replace(':', '')
		try:
			lect_hours = int(subj.split('   ')[1].replace('(л)', ''))
		except:
			lect_hours = 0
		try:
			prac_hours = int(subj.split('   ')[2].replace('(пр)', ''))
		except:
			prac_hours = 0
		try:
			lab_hours = int(subj.split('   ')[3].replace('(лаб)\n', ''))
		except:
			try:
				lab_hours = int(subj.split('   ')[3].replace('(лаб)', ''))
			except:
				lab_hours = 0
		sub_dict.update({name_sub: (lect_hours + prac_hours + lab_hours)})
		print(sub_dict)

# Расчет прибыли фирм
import json

with open('firms.txt', 'r', encoding = 'UTF-8') as firms:
	firms_list_final = []
	firms_names = []
	firms_profits = []
	firms_profits_all = []
	for firm in firms:
		firms_names.append(firm.split(' ')[0])
		cashflow = int(firm.split(' ')[2])
		costs = int(firm.split(' ')[3])
		firms_profits_all.append(cashflow - costs)
		if costs < cashflow:
			firms_profits.append(cashflow - costs)
average_prof = {'average_profit': (sum(firms_profits)/len(firms_profits))}
number = 0
firms_list = {}
for lenth in range(len(firms_names)):
	firms_list.update({firms_names[number]: firms_profits_all[number]})
	number += 1
firms_list_final.append(firms_list)
firms_list_final.append(average_prof)
print(firms_list_final)

with open('firms.json', 'w', encoding = "UTF-8") as js:
	json.dump(firms_list_final, js)

with open('firms.json', 'r', encoding = "UTF-8") as js:
	new_dict = json.load(js)
print(new_dict)