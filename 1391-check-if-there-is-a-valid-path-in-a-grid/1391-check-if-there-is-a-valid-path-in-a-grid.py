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
            neighbors = {
                1: [(0, -1, {1, 4, 6}), (0, 1, {1, 3, 5})],
                2: [(-1, 0, {2, 5, 6}), (1, 0, {2, 3, 4})],
                3: [(0, -1, {1, 4, 6}), (1, 0, {2, 5, 6})],
                4: [(1, 0, {2, 5, 6}), (1, 0, {2, 3, 4})],
                5: [(-1, 0, {2, 3, 4}), (0, -1, {1, 4, 6})],
                6: [(-1, 0, {2, 3, 4}), (0, 1, {1, 3, 5})]
            }

            for dx, dy, valid_neighbors in neighbors[val]:
                new_row, new_col = row + dx, col + dy
                if isValidPosition(grid, (new_row, new_col)) and grid[new_row][new_col] in valid_neighbors:
                    union(rep, size, (row, col), (new_row, new_col))

        
        def solution(rep, node1, node2):
            node1, node2 = find(rep, node1), find(rep, node2)
            return node1 == node2
        
        for row in range(rows):
            for col in range(cols):
                check(grid, row, col)
        
        return solution(rep, (0, 0), (rows - 1, cols - 1))