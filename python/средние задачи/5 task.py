def find_perfect_numbers(limit):
    perfect_numbers = []
    
    for num in range(2, limit + 1):
        divisors_sum = 0
        
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
  
        if divisors_sum == num:
            perfect_numbers.append(num)
    
    return perfect_numbers

limit = int(input ("Установите диапазон меньше 1000: "))
perfect_numbers = find_perfect_numbers(limit)
print(f"Совершенные числа в диапазоне от 0 до {limit}: {perfect_numbers}")
