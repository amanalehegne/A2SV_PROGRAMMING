class Solution:    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        length = rows * cols

        left = 0
        right = length - 1
        while left <= right:
            midPoint = (left + right) // 2
            row = midPoint // cols
            col = midPoint % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = midPoint - 1
            else:
                left = midPoint + 1
        return False
        