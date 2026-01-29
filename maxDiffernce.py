def max_difference(arr):
    if not arr:
        return None  # handle empty array case
    return max(arr) - min(arr)

# Example usage
arr = [2, 8, 1, 10, 5]
print("Maximum difference:", max_difference(arr))
