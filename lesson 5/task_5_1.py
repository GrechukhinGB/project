## Задание №1 Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

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