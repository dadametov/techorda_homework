def median(array):
    if not array:
        return None  
    
    sorted_array = sorted(array)
    n = len(sorted_array)
 
    mid = n // 2  
    
    if n % 2 == 0: 
        return sorted_array[mid - 1]  
    else: 
        return sorted_array[mid]  

input_array = [1, 2, 3]
print(median(input_array))  
