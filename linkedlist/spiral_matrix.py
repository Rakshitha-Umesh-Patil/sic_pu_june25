def spiral_matrix(m, n):
    matrix = []
    count = 1
    for _ in range(m):
        row = []
        for _ in range(n):
            row.append(count)
            count += 1
        matrix.append(row)

    print("\nGenerated Matrix:")
    for row in matrix:
        print(row)

    print("\nSpiral Order:")
    top, bottom = 0, m - 1
    left, right = 0, n - 1

    while top <= bottom and left <= right:
       
        for i in range(left, right + 1):
            print(matrix[top][i], end=" ")
        top += 1

        
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=" ")
        right -= 1

        if top <= bottom:
            
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1

        if left <= right:
            
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=" ")
            left += 1
    print()

if __name__ == "__main__":
    m = int(input("Enter number of rows (M): "))
    n = int(input("Enter number of columns (N): "))
    spiral_matrix(m, n)
