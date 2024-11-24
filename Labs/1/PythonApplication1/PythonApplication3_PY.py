### Программа с использованием всякого разного из методички ###

def is_prime(n):
    """Проверка, является ли число простым."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

max_attempts = 5
attempts = 0

while attempts < max_attempts:
    user_input = input("Введите число для проверки на простоту: ")
    
    try:
        number = int(user_input)
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    if is_prime(number):
        print(f"{number} является простым числом.")
        break
    else:
        print(f"{number} не является простым числом.")
        attempts += 1
        if attempts < max_attempts:
            print(f"Попробуйте еще раз. Осталось попыток: {max_attempts - attempts}")
        else:
            print("Вы исчерпали все попытки.")

print("\nСписок простых чисел от 1 до 50:")
primes = [num for num in range(1, 51) if is_prime(num)]
for index, prime in enumerate(primes):
    print(f"{index + 1}: {prime}")
