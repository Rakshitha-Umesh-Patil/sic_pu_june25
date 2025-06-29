num = input("Enter a number: ")
max_digit = 0

for ch in num:
    digit = int(ch)
    if digit > max_digit:
        max_digit = digit

print("Biggest digit is:", max_digit)
