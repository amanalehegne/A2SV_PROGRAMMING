class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        oneRow = []
        zeroRow = []
        for row in grid:
            one = zero = 0
            for num in row:
                if num:
                    one += 1
                else:
                    zero += 1
            oneRow.append(one)
            zeroRow.append(zero)

        oneCol = []
        zeroCol = []
        rows = len(grid)
        cols = len(grid[0])
        for index in range(cols):
            one = zero = 0
            for i in range(rows):
                num = grid[i][index]
                if num:
                    one += 1
                else:
                    zero += 1
            oneCol.append(one)
            zeroCol.append(zero)

        difference = [[0] * cols for i in range(rows)]
        for row in range(rows):
            for col in range(cols):
                difference[row][col] = (oneRow[row] + oneCol[col] - zeroRow[row] - zeroCol[col])

        return difference
        