num = input("Enter a number: ")

sum_odd_pos_digits = 0
for i in range(len(num)):
    digit=int(num[i])
    if (i + 1) % 2 != 0 and digit % 2==0 :  
        sum_odd_pos_digits += digit

print("Sum of digits at even positions :", sum_odd_pos_digits)
