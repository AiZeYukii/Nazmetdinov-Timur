#   Вводные данные
number = 1264174

#   Проверка с использованием логических операторов
if number > 1000000 and number < 2000000:
    print(f"{number} находится в диапазоне от 1,000,000 до 2,000,000.")
elif number < 1000000 or number > 2000000:
    print(f"{number} находится вне диапазона от 1,000,000 до 2,000,000.")
else:
    print(f"{number} равно границе диапазона.")

#   Дополнительная проверка
if number % 2 == 0 and number > 0:
    print(f"{number} - четное положительное число.")
elif number % 2 != 0 and number > 0:
    print(f"{number} - нечетное положительное число.")
else:
    print(f"{number} - отрицательное число.")
