def create_range(n):
    if n <= 0 or n > 10000:
        raise ValueError("n должно быть в диапазоне 1 <= n <= 10000")
    
    return [i for i in range(1, n + 1)]


arr = create_range(5)
print(arr)  
