def count_leap_years(n):
    # Считаем количество високосных лет по правилам
    leap_years = (n // 4) - (n // 100) + (n // 400)
    return leap_years

# Ввод числа n
n = int(input("Введите год: "))

# Вывод результата
print(count_leap_years(n))
