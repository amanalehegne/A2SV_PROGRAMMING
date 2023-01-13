class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        zeros = set()
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zeros.add((row, col))

        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for x, y in moves:
            for zero in zeros:
                row, col = zero
                while (0 <= row < rows) and (0 <= col < cols):
                    matrix[row][col] = 0
                    row, col = row + x, col + y
        