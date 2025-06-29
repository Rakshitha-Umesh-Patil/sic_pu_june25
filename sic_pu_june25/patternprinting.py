n = int(input("Enter number of lines: "))

# Right Angled Triangle
for i in range(1, n + 1):
    print("*" * i)

#  Equilateral Triangle
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i+1))