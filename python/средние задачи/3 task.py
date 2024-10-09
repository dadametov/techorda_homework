# Функция для проверки, является ли число простым
def is_prime(n):
    if n <= 1:  
        return False
    for i in range(2, int(n ** 0.5) + 1):  # делители до квадратного корня из n
        if n % i == 0:
            return False
    return True

# ввод числа
number = int(input("Введите число: "))

# вывод
if is_prime(number):
    print(f"Число {number} является простым.")
else:
    print(f"Число {number} не является простым.")
