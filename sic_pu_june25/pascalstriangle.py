rows = int(input("Enter number of rows: "))

for i in range(rows):
    
    print(" " * (rows - i), end="")

    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()
