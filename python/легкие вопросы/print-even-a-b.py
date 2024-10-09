###print-even-a-b
#Вывести в консоль четные числа в диапазоне от a включительно до b включительно.
#Sample Input:
#0 4
#Sample Output:
#0 2 4

def print_even_a_b(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=' ')

a, b = 0, 4
print_even_a_b(a, b)

