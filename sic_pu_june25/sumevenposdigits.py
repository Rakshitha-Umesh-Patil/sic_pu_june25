num = input("Enter a number: ")

sum_even_pos_digits = 0
for i in range(len(num)):
    if (i + 1) % 2 == 0: 
        sum_even_pos_digits += int(num[i])

print("Sum of digits at even positions (from left):", sum_even_pos_digits)
