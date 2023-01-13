class Solution:
    def matrixThree(self, x, y, matrix):
        maxVal = 0
        for i in range(3):
            for j in range(3):
                maxVal = max(maxVal, matrix[x + i][y + j])
        return maxVal
    
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        res = [[0] * (cols - 2) for i in range(rows - 2)]

        for row in range(rows - 2):
            for col in range(cols - 2):
                res[row][col] = self.matrixThree(row, col, grid)

        return res
        