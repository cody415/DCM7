def find_missing_number(arr, n):
    # Expected sum of numbers from 1 to n
    total_sum = n * (n + 1) // 2
    
    # Actual sum of the given array
    arr_sum = sum(arr)
    
    # Missing number
    return total_sum - arr_sum

# Example usage
