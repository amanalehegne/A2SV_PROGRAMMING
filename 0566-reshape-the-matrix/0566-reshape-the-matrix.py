class Solution:
    def matrixReshape(self, matrix: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        if r * c != rows * cols:
            return matrix
        
        res = [[0] * c for i in range(r)]
        
        for i in range(r * c):
            row = i // len(matrix[0])
            col = i % len(matrix[0])
            rowIndex = i // c
            colIndex = i % c
            res[rowIndex][colIndex] = matrix[row][col]
        return res