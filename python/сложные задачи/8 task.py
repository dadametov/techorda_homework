def stock_buy(m, prices):
    price_index_map = {}  # Словарь для хранения цен и их индексов
    
    for index, price in enumerate(prices):
        # Вычисляем, сколько денег нужно для достижения суммы m
        complement = m - price
        
        # Проверяем, есть ли нужная цена в словаре
        if complement in price_index_map:
            # Возвращаем отсортированные индексы
            return sorted([price_index_map[complement], index])
        
        # Добавляем текущую цену и ее индекс в словарь
        price_index_map[price] = index

# Пример использования
m = 3
s = [1, 2, 3]
result = stock_buy(m, s)
print(result)  # Вывод: [1, 3]
