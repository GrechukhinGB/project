## 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

a = input('Введите первую букву: ')
b = input('Введите первую букву: ')
a1 = int(ord(a) - ord('a') + 1)
b2 = int(ord(b) - ord('a') + 1)
c = b2 - a1
print(f'Буква "{a}" стоит на месте {a1}, '
      f'буква "{b}" стоит на месте {b2}, '
      f'между ними {c} букв')