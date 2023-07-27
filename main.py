from funcs import pluc
from funcs import minus


number_one = input("Введите первое число")
number_two = input("Введите второе число")

choice = int(input('''Введите номер операции
Сложение - 1
Вычитание - 2'''))

if choice == 1:
    summa = pluc(number_one, number_two)
    print(summa)
elif choice == 2:
    subtraction= minus(number_one, number_two)
    print(subtraction)
else:
    print('неизвестная команда')