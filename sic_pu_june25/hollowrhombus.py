n = int(input("Enter number of lines: "))

for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    