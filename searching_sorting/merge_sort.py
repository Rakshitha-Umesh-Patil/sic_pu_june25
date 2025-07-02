def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2   # Find the middle
        left = arr[:mid]      # Split left half
        right = arr[mid:]     # Split right half

        # Recursively sort both halves
        merge_sort(left)
        merge_sort(right)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left in left[]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Checking if any element was left in right[]
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)
