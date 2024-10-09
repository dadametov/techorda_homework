def calc_deposit(n, k, b):
    # Проверка на соответствие ограничениям
    if not (0 <= n <= 10000):
        raise ValueError("n должно быть в диапазоне 0 <= n <= 10000")
    if not (0 <= k <= 100):
        raise ValueError("k должно быть в диапазоне 0 <= k <= 100")
    if not (0 <= b <= 10000):
        raise ValueError("b должно быть в диапазоне 0 <= b <= 10000")
    
    for _ in range(n):
        b += b * (k / 100)
    return b

# Пример вызова функции
n, k, b = 1, 5, 1000
print(calc_deposit(n, k, b))
