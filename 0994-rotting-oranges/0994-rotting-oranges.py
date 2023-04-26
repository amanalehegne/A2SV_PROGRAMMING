class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def inRange(row, col):
            if (0 <= row < len(grid)) and (0 <= col < len(grid[0])):
                return True
            return False
        
        
        dir_ = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        rows = len(grid)
        cols = len(grid[0])
        
        start = []
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    start.append([row, col])
                if grid[row][col] == 1:
                    count += 1
                    
        
        queue = deque(start)
        res = 0
        seen = set()
        
        
        while queue:
            level = len(queue)
            for i in range(level):
                row, col = queue.popleft()
                seen.add((row, col))
                for row_, col_ in dir_:
                    newRow = row + row_
                    newCol = col + col_
                    if inRange(newRow, newCol) and ((newRow, newCol) not in seen) and grid[newRow][newCol] == 1:
                        count -= 1
                        if count == 0:
                            return res + 1
                        queue.append([newRow, newCol])
                        grid[newRow][newCol] = 2
            res += 1
        if count > 0:
            return -1
        return 0
            