num = input("Enter a number: ")
smallest_digit=9
sec_smallest_digit =9

for ch in num:
    digit = int(ch)
    if digit <= smallest_digit:
        smallest_digit = digit
    elif digit < sec_smallest_digit:
        sec_smallest_digit=digit
print("Second smallest  digit is:", sec_smallest_digit)
