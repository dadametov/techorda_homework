def miss_you(array1, array2):
    set_array1 = set(array1)

    missing_numbers = [num for num in array2 if num not in set_array1]
    
    return sorted(missing_numbers)

# Sample Input
array1 = [1, 1, 3, 2, 5]
array2 = [1, 3, 9, 1, 5, 7]
print(miss_you(array1, array2))  # Output: [7, 9]
