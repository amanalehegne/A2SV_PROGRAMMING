class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def check(row, col):
            return (0 <= row < len(grid1)) and (0 <= col < len(grid1[0]))
        
        dir_ = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def DFS(grid, row, col):
            checkValid = True
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()
                grid[row][col] = -1
                if grid1[row][col] != -1:
                    checkValid = False
                for r, c in dir_:
                    newRow, newCol = row + r, col + c
                    if check(newRow, newCol) and grid[newRow][newCol] == 1:
                        stack.append((newRow, newCol))
            
            return checkValid
        
        
        rows = len(grid1)
        cols = len(grid1[0])
        island = 0
        for row in range(rows):
            for col in range(cols):
                if grid1[row][col] == 1:
                    DFS(grid1, row, col)
                    island += 1
        
        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1:
                    if DFS(grid2, row, col):
                        res += 1
                    
        
        return res
            