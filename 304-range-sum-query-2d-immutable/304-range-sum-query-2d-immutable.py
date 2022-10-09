class NumMatrix:

    def __init__(self, matrix):
        row, col = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (col + 1) for i in range(row + 1)]

        # Create box prefix sum
        for r in range(row):
            prefix_sum = 0
            for c in range(col):
                prefix_sum += matrix[r][c]
                self.prefix_sum[r + 1][c + 1] = prefix_sum + self.prefix_sum[r][c + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        area_sum = self.prefix_sum[row2 + 1][col2 + 1]
        remove_top = self.prefix_sum[row1][col2 + 1]
        remove_side = self.prefix_sum[row2 + 1][col1]
        double_removed = self.prefix_sum[row1][col1]
        return area_sum - remove_top - remove_side + double_removed
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)