def find_subarray_with_min_difference(arr, k):
    left = 0
    right = k - 1
    min_diff = float('inf')
    min_diff_indices = (0, k - 1)
    
    # Найдем начальную разность между максимальным и минимальным в первом подмассиве
    current_diff = max(arr[left:right+1]) - min(arr[left:right+1])
    min_diff = current_diff
    
    # Перемещаем указатели и обновляем разность
    while right < len(arr) - 1:
        right += 1
        left += 1
        
        current_diff = max(arr[left:right+1]) - min(arr[left:right+1])
        
        # Обновляем минимальную разность и индексы подмассива
        if current_diff < min_diff:
            min_diff = current_diff
            min_diff_indices = (left, right)
    
    return arr[min_diff_indices[0]: min_diff_indices[1] + 1]

# Пример использования
arr = [1, 5, 3, 19, 18, 25]
k = 3
result = find_subarray_with_min_difference(arr, k)
print("Подмассив с минимальной разностью между max и min:", result)
