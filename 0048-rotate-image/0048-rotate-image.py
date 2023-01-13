class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        cols = rows = len(matrix)
        for row in range(rows):
            for col in range(cols - row):
                index = cols - 1 - col
                matrix[index][row], matrix[row][index] = matrix[row][index], matrix[index][row]
        for row in range(rows):
            for col in range(cols // 2 + cols % 2):
                index = cols - 1 - col
                matrix[row][col], matrix[row][index] = matrix[row][index], matrix[row][col]
        return matrix
            
        