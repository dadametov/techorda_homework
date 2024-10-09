import math


def is_perfect_square(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n


def is_fibonacci_number(n):
    expr1 = 5 * n * n + 4
    expr2 = 5 * n * n - 4
 
    return is_perfect_square(expr1) or is_perfect_square(expr2)

n = int(input("Введите число: "))
if is_fibonacci_number(n):
    print(f"Число {n} является числом Фибоначчи.")
else:
    print(f"Число {n} не является числом Фибоначчи.")
