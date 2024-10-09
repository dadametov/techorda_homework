def swap_bits(a):
    # Получаем старшие 4 бита
    high_bits = a >> 4
    # Получаем младшие 4 бита
    low_bits = a & 0x0F
    # Меняем местами старшие и младшие биты
    result = (low_bits << 4) | high_bits
    return result

# Ввод числа
a = int(input("Введите число: "))

# Вывод результата
print(swap_bits(a))
