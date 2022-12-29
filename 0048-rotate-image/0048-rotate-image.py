class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
            inner = length - i
            for j in range(inner):
                index = length - 1 - j
                matrix[index][i], matrix[i][index] = matrix[i][index], matrix[index][i]
        for i in matrix:
            left = 0
            right = len(i) - 1
            while left < right:
                i[left], i[right] = i[right], i[left]
                left += 1
                right -= 1
            
        