class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            temp = matrix[row][col]
            
            if temp == target:
                return True
            elif temp < target:
                row += 1
            else:
                col -= 1
                
        return False