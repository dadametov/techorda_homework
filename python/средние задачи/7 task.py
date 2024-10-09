def is_perfect_number(n):
    if n <= 1:
        return False
    
    divisors_sum = 0

    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    return divisors_sum == n

n = int(input("Введите число: "))

if is_perfect_number(n):
    print(f"Число {n} является совершенным числом.")
else:
    print(f"Число {n} не является совершенным числом.")
