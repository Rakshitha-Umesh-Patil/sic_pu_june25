nums = [6,7,8,3,4]
smallest = nums[0]
largest = nums[0]

for num in nums:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Smallest:", smallest)
print("Largest:", largest)
