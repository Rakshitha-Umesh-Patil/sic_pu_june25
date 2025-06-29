m = int(input("Enter m: "))
n = int(input("Enter n: "))

if m < n:
    print("Prime numbers in decreasing order:")
    for i in range(n, m - 1, -1):
        is_prime = True
        if i < 2:
            continue
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")
else:
    print("Invalid input: m should be less than n")

