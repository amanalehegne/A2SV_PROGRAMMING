class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        for row in range(rows - 2):
            for col in range(cols - 2):
                matrix = []
                checkDuplicate = set()
                for i in range(row, row + 3):
                    arr = []
                    for j in range(col, col + 3):
                        arr.append(grid[i][j])
                        if 1 <= grid[i][j] <= 9:
                            checkDuplicate.add(grid[i][j])
                    matrix.append(arr)
                if self.getSums(matrix) == 1 and len(checkDuplicate) == 9:
                    count += 1
        
        return count
                    
                
                
                
    def getSums(self, matrix):
        sumVals = set()
        for row in range(3):
            rowSum = colSum = 0
            for col in range(3):
                rowSum += matrix[row][col]
                colSum += matrix[col][row]
            sumVals.add(rowSum)
            sumVals.add(colSum)

        #Diagonal
        diagonalSum = [0, 0]
        for row in range(3):
            idx = 2 - row
            diagonalSum[0] += matrix[row][idx]
            diagonalSum[1] += matrix[row][row]
        sumVals.add(diagonalSum[0])
        sumVals.add(diagonalSum[1])

        return len(sumVals)
        