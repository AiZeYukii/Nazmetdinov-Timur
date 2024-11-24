#   Вводные данные
number = 1264174

#   Числа для сравнения
comparison_numbers = [1000000, 1264174, 2000000]

#   Операторы сравнения(сравнивают)
for compare_number in comparison_numbers:
    if number > compare_number:
        print(f"{number} больше {compare_number}")
    elif number < compare_number:
        print(f"{number} меньше {compare_number}")
    else:
        print(f"{number} равно {compare_number}")
