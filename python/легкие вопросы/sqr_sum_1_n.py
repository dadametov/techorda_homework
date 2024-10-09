##Циклы
###sqr-sum-1-n
#Вернуть сумму квадратов чисел от 1 до n включительно.
#Ограничения
#1 <= n <= 10860

def sqr_sum_1_n(n):
    return sum(i ** 2 for i in range(1, n + 1))

n = 3
print(sqr_sum_1_n(n))
