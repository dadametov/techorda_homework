def sort_three_numbers(a, b, c):
    if a > b:
        a, b = b, a  
    if a > c:
        a, c = c, a  
    if b > c:
        b, c = c, b  

    print(a, b, c)

# Ввод трех чисел
a, b, c = map(int, input("Введите три числа через пробел: ").split())

# Вывод отсортированных чисел
sort_three_numbers(a, b, c)
