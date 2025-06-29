n= int(input("Enter number of lines: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")  # Border
        elif j == i or j == n - i - 1:
            if n % 2 == 1 and i == n // 2 and j == n // 2:
                print("0", end="")  # Center
            else:
                print("*", end="")  # X shape
        else:
            print(" ", end="")  # Inside empty
    print()