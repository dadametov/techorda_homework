def bubble_sort(arr):
    n = len(arr)
    if not (0 <= n <= 10000):  # Проверка на ограничения длины массива
        raise ValueError("Длина массива должна быть в диапазоне 0 <= array.length <= 10000")
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Пример вызова функции
arr = [7, 5, 93, 1, 4]
bubble_sort(arr)
print(arr) 
