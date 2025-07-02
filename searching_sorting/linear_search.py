def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  


arr = [5, 3, 7, 1, 9]
target = 7
result = linear_search(arr, target)
print("Element found at index:" if result != -1 else "Not found", result)
