def sum_array(arr):
    if not (0 <= len(arr) <= 10000):  
        raise ValueError("Длина массива должна быть в диапазоне 0 <= array.length <= 10000")
    
    return sum(arr)


arr = [7, 5, 9, 1, 4]
sum_number = sum_array(arr)
print(sum_number)  
