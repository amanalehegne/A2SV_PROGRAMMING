class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        def checkValid(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                return True
            return False
        
        dir_ = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        if grid[0][0] == 1:
            return -1
        
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1
        
        ans = [len(grid) - 1, len(grid[0]) - 1]
        res = float("inf")
        
        while queue:
            val = queue.popleft()
            if [val[0], val[1]] == ans:
                return val[-1]
            
            for x, y in dir_:
                row = val[0] + x
                col = val[1] + y
                count = val[-1]
                
                if checkValid(row, col) and grid[row][col] == 0:
                    grid[row][col] = 1
                    queue.append((row, col, count + 1))
        
        return -1
                    