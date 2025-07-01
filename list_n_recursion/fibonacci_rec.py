def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Print first N terms
N = int(input("Enter number of terms: "))
for i in range(1, N + 1):
    print(fibonacci(i), end=' ')

