# Переменные
var1 = 1234
print(var1)
var2 = 'Вариант'
print(var2)

# Ввод значений и вывод на экран
name = input('Введите ваше имя: ')
age = input("Введите ваш возраст: ")
prof = input('Ваша профессия: ')
prof_exp = input('Стаж работы по профессии: ')

print(f'Имя: {name}.\nВозраст: {age}.\nПрофессия: {prof}.\nСтаж: {prof_exp}.')

# Время в секундах
time = input('Введите время в секундах: ')
try:
    if int(time)//3600 < 10:
        time_hours = f'0{int(time) // 3600}'
    else:
        time_hours = int(time) // 3600
    if int(time)%3600//60 < 10:
        time_minutes = f'0{int(time) % 3600 // 60}'
    else:
        time_minutes = int(time) % 3600 // 60
    if int(time)%3600%60 < 10:
        time_seconds = f'0{int(time) % 3600 % 60}'
    else:
        time_seconds = int(time) % 3600 % 60
except:
    print("Были введены некорректные данные, введите только число")
print(f'{time_hours}:{time_minutes}:{time_seconds}')

# Число n
n = input("Введите число: ")
fin_number = int(n) + int(n + n) + int(n + n + n)
print(fin_number)

# Наибольшая цифра в числе
num = int(input("Введите число: "))
max = num % 10
next = num // 10
while next > 0:
    if next % 10 > max:
        max = next % 10
    next = next // 10
print(f'Наибольшая цифра в числе: {max}')

# Оценка компании
revenue = int(input('Введите выручку вашего предприятия: '))
cost = int(input('Введите сумму издержек вашего предприятия: '))
if revenue > cost:
    print(f'Фирма работает с положительным финансовым результатом: {revenue - cost}')
else:
    print(f'Фирма работает с отрицательным финансовым результатом: {revenue - cost}')
if revenue > cost:
    print(f'Рентабельность компании составляет: {(revenue - cost)/revenue}')
    workers_num = int(input('Введите количество работников вашего предприятия: '))
    inc_per_worker = (revenue-cost)/workers_num
    print(f'Прибыль фирмы на одного сотрудника: {inc_per_worker}')

# Результаты спортсмена
a = int(input('Введите начальный результат пробежки спортсмена: '))
b = int(input('Введите желаемый результат пробежки спортсмена: '))
for n in range(1, 9999):
    a = a + (a / 10)
    if a >= b:
        print(f'На {n} день спортсмен достиг результата - не менее {b} км.')
        break