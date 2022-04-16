<<<<<<< refs/remotes/origin/main
## Задание №1 Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
=======
## Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
>>>>>>> lesson 5
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple
<<<<<<< refs/remotes/origin/main

Enterprise = namedtuple('Предприятие', 'название q1 q2 q3 q4 итого')

enterprises_count = int(input('Введите количество предприятий для анализа: '))

enterprises = []
total_income_for_all = 0

for i in range(enterprises_count):
    name = input(f'Введите название {i + 1} предприятия: ')
    q1 = float(input(f'Введите название {i + 1} предприятия: '))
    q2 = float(input(f'Введите название {i + 1} предприятия: '))
    q3 = float(input(f'Введите название {i + 1} предприятия: '))
    q4 = float(input(f'Введите название {i + 1} предприятия: '))
    total = q1 + q2 + q3 + q4
    total_income_for_all += total
    enterprises.append(Enterprise(name, q1, q2, q3, q4, total))

average_income = total_income_for_all / enterprises_count

print(f'Средний доход: {average_income}')

above_average_income = []
below_average_income = []

for enterprise in enterprises:
    if enterprise.total < average_income:
        below_average_income.append(enterprise.name)
    else:
        above_average_income.append(enterprise.name)

print('Выше среднего:')
print(*above_average_income, sep='\n')
print('Ниже среднего:')
print(*below_average_income, sep='\n')
=======
from statistics import mean

New_Company = namedtuple('New_Company', 'name profit_list avg')

lst = []
for i in range(int(input('Введите количество компаний: '))):
    arg = input('Введите в строку имя и поквартальную прибыль через пробел:\n').split()
    lst.append(New_Company(arg[0], arg[1:], mean(map(int, arg[1:3]))))

avg = mean([i.avg for i in lst])

for i in lst:
    print(f'Компания: {i.name} \t\tСредняя прибыль за год: {i.avg}')

print('_' * 70, '\n')

print('Компании с прибылью меньше средней:')
for i in lst:
    if i.avg < avg:
        print(i.name)

print('Компании с прибылью больше средней:')
for i in lst:
    if i.avg > avg:
        print(i.name)
>>>>>>> lesson 5
