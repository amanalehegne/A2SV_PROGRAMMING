class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        size = col * row
        s, index = 0, 0
        ans = []
        while s < size:
            i = 0 + index
            j = 0 + index
            while j < col and s < size:
                ans.append(matrix[i][j])
                j += 1
                s += 1
            j -= 1
            i += 1
            while i < row and s < size:
                ans.append(matrix[i][j])
                i += 1
                s += 1
            i -= 1
            j -= 1
            while j >= index and s < size:
                ans.append(matrix[i][j])
                j -= 1
                s += 1
            i -= 1
            j += 1
            while i > index and s < size:
                ans.append(matrix[i][j])
                i -= 1
                s += 1
            col -= 1
            row -= 1
            index += 1
        return ans