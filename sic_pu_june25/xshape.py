n=int(input("Enter number of lines"))

for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()