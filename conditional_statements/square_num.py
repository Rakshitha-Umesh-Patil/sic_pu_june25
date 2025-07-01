num = int(input("Enter a positive number: "))

if num >= 0:
    x = int(num ** 0.5)
    if x * x == num:
        print("Perfect square")
    else:
        print("Not a perfect square")
else:
    print("Not a positive number")
