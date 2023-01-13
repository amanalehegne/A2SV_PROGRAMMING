def moveBishop(matrix):
    cols = len(matrix[0])
    rows = len(matrix)

    for i in range(cols):
        col, row = i, 0
        prev = None
        while col < cols and row < rows:
            if (prev is not None) and (prev != matrix[row][col]):
                return False
            prev = matrix[row][col]
            col, row = col + 1, row + 1
        prev = None
        if i != 0:
            row, col = i, 0
            while col < cols and row < rows:
                if (prev is not None) and (prev != matrix[row][col]):
                    return False
                prev = matrix[row][col]
                col, row = col + 1, row + 1

    return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(moveBishop(matrix))

