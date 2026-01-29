def min_flips(arr):
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    
    # Minimum flips needed
    return min(count_0, count_1)

# Example usage
arr = [1, 0, 1, 1, 0, 0, 1]
print("Minimum flips needed:", min_flips(arr))
