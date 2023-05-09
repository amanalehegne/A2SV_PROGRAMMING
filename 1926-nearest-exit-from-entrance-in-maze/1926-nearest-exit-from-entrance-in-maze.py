class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def isValidPosition(graph, node):
            return 0 <= node[0] < len(graph) and 0 <= node[1] < len(graph[0])


        def BFS(graph, node, seen):
            root = tuple(node)
            queue = deque([root])

            neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            level = 0

            while queue:
                size = len(queue)
                for _ in range(size):
                    row_, col_ = queue.popleft()
                    currentNode = (row_, col_)

                    if currentNode not in seen:

                        if (currentNode != root) and ((row_ == len(graph) - 1) or (row_ == 0) or (col_ == len(graph[0]) - 1) or (col_ == 0)):
                            return level
                        seen.add(currentNode)

                        for r, c in neighbours:
                            row, col = row_ + r, col_ + c
                            nextNode = (row, col)
                            if isValidPosition(graph, nextNode) and graph[row][col] == ".":
                                queue.append(nextNode)
                level += 1
            return -1
        
        seen = set()
        return BFS(maze, entrance, seen)