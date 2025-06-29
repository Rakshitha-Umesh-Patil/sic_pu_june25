num = input("Enter a number: ")
prime_count = 0

for ch in num:
    digit = int(ch)
    if digit < 2:
        continue  # skip 0 and 1
    is_prime = True
    for i in range(2, digit):
        if digit % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1

print("Number of prime digits:", prime_count)
