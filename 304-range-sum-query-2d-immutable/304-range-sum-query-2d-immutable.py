class NumMatrix:

    def __init__(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (cols + 1) for r in range(rows + 1)]

        # Prefix sum
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.prefix_sum[r][c + 1]
                self.prefix_sum[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total_area = self.prefix_sum[row2 + 1][col2 + 1]
        num1 = self.prefix_sum[row1][col2 + 1]
        num2 = self.prefix_sum[row2 + 1][col1]
        left_out = self.prefix_sum[row1][col1]
        return total_area + left_out - num1 - num2



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)