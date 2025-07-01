nums = [1, 2, 2, 3, 1, 4]
unique = []

for num in nums:
    is_duplicate = False
    for u in unique:
        if u == num:
            is_duplicate = True
            break
    if not is_duplicate:
        unique.append(num)

print("List without duplicates:", unique)
