class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        def isValidPosition(grid, node):
            return 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0])
        
        def BFS(grid, queue, seen):
            dir_ = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            level = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    row_, col_ = queue.popleft()
                    current = (row_, col_)
                    if current not in seen:
                        seen.add(current)
                        for r, c in dir_:
                            row, col = row_ + r, col_ + c
                            nextNode = (row, col)
                            if isValidPosition(grid, nextNode) and (grid[row][col] == 1) and (nextNode not in seen):
                                queue.append(nextNode)
                                
                level += 1
                
        def BFS2(grid, queue, seen, visited):
            dir_ = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            level = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    row_, col_ = queue.popleft()
                    current = (row_, col_)
                    if current not in seen:
                        seen.add(current)
                        for r, c in dir_:
                            row, col = row_ + r, col_ + c
                            nextNode = (row, col)
                            if isValidPosition(grid, nextNode) and (nextNode not in seen):
                                if (nextNode not in visited) and grid[row][col] == 1:
                                    return level
                                if grid[row][col] == 0:
                                    queue.append(nextNode)

                level += 1
            return level
        
        def findNode(grid):
            n = len(grid)
            for row in range(n):
                for col in range(n):
                    if grid[row][col] == 1:
                        return (row, col)
        
        node = findNode(grid)
        queue = deque([node])
        seen = set()
        x = BFS(grid, queue, seen)
        
        queue = deque(list(seen))
        
        return BFS2(grid, queue, set(), seen)