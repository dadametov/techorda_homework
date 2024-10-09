def perfectly_balanced(array):
    total_sum = sum(array)  # Общая сумма массива
    left_sum = 0  # Инициализируем сумму слева
    
    for i in range(len(array)):
        # Проверяем, если сумма слева равна сумме справа
        if left_sum == (total_sum - left_sum - array[i]):
            return True  # Суммы равны, возвращаем True
        
        # Обновляем сумму слева
        left_sum += array[i]
    
    return False  # Если не нашли сбалансированный элемент, возвращаем False

input_array = [1, 2, 9, 8, 5, 7]
print(perfectly_balanced(input_array))  # Вывод: True
