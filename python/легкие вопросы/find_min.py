def find_min(arr):
    if len(arr) == 0:  
        return 0
    
    min_value = arr[0]  
    
    for num in arr: 
        if num < min_value:  
            min_value = num
    
    return min_value


arr = [1, 2, 3]
print(find_min(arr))  
