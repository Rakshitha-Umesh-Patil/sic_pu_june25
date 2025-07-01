def list_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + list_sum(lst[1:])

nums = [1, 2, 3, 4]
print("Sum:", list_sum(nums))
