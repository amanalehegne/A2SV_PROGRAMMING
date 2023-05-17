class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        
        rep = dict()
        size = dict()
        for row in range(rows):
            for col in range(cols):
                rep[(row, col)]  = (row, col)
                size[(row, col)] = 1
        
        def find(rep, node):
            if node == rep[node]:
                return node
            rep[node] = find(rep, rep[node])
            return rep[node]
        
        def union(rep, size, node1, node2):
            node1 = find(rep, node1)
            node2 = find(rep, node2)
            
            if node1 == node2:
                return
            size1, size2 = size[node1], size[node2]
            if size1 > size2:
                node1, node2 = node2, node1
            
            rep[node1] = node2
            size[node2] += size[node1]
        
        def isValidPosition(grid, node):
            return 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0])

        def check(grid, row, col):
            val = grid[row][col]
            right = {1, 4, 6}
            left = {1, 3, 5}
            upper = {2, 5, 6}
            lower = {2, 3, 4}
            
            if val == 1:
                if isValidPosition(grid, (row, col - 1)) and grid[row][col - 1] in right:
                    union(rep, size, (row, col), (row, col - 1))
                if isValidPosition(grid, (row, col + 1)) and grid[row][col + 1] in left:
                    union(rep, size, (row, col), (row, col + 1))
            elif val == 2:
                if isValidPosition(grid, (row - 1, col)) and grid[row - 1][col] in lower:
                    union(rep, size, (row, col), (row - 1, col))
                if isValidPosition(grid, (row + 1, col)) and grid[row + 1][col] in upper:
                    union(rep, size, (row, col), (row + 1, col))
            elif val == 3:
                if isValidPosition(grid, (row, col - 1)) and grid[row][col - 1] in right:
                    union(rep, size, (row, col), (row, col - 1))
                if isValidPosition(grid, (row + 1, col)) and grid[row + 1][col] in upper:
                    union(rep, size, (row, col), (row + 1, col))
            elif val == 4:
                if isValidPosition(grid, (row + 1, col)) and grid[row + 1][col] in right:
                    union(rep, size, (row, col), (row + 1, col))
                if isValidPosition(grid, (row + 1, col)) and grid[row + 1][col] in upper:
                    union(rep, size, (row, col), (row + 1, col))
            elif val == 5:
                if isValidPosition(grid, (row - 1, col)) and grid[row - 1][col] in lower:
                    union(rep, size, (row, col), (row - 1, col))
                if isValidPosition(grid, (row, col - 1)) and grid[row][col - 1] in right:
                    union(rep, size, (row, col), (row, col - 1))
            elif val == 6:
                if isValidPosition(grid, (row - 1, col)) and grid[row - 1][col] in lower:
                    union(rep, size, (row, col), (row - 1, col))
                if isValidPosition(grid, (row, col + 1)) and grid[row][col + 1] in left:
                    union(rep, size, (row, col), (row, col + 1))
        
        def solution(rep, node1, node2):
            node1, node2 = find(rep, node1), find(rep, node2)
            return node1 == node2
        
        for row in range(rows):
            for col in range(cols):
                check(grid, row, col)
        
        return solution(rep, (0, 0), (rows - 1, cols - 1))