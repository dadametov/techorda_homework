###pow-a-b
#Вернуть число a в степени b. Используя цикл.
#Ограничения
#b > 0
#a^b входит в ограничения типа int
#Sample Input:
#2 6
#Sample Output:
#64

def pow_a_b(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

a, b = 2, 6
print(pow_a_b(a, b))
