a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b:
    if a < c:
        print("Smallest is:", a)
    else:
        print("Smallest is:", c)
else:
    if b < c:
        print("Smallest is:", b)
    else:
        print("Smallest is:", c)
