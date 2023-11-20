class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def dijkstra(graph, rows, cols):
            distances = [[float('inf')] * cols for _ in range(rows)]
            distances[0][0] = 0
            visited = set()

            priority_queue = [(0, (0, 0))]
            while priority_queue:
                current_val, current_node = heapq.heappop(priority_queue)

                if current_node not in visited:
                    if current_node == (rows - 1, cols - 1):
                        return distances[-1][-1]

                    visited.add(current_node)

                    for neighbor, weight in graph[current_node]:
                        row, col = neighbor

                        distance = max(current_val, weight)
                        if distance < distances[row][col]:
                            distances[row][col] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))
            return distances[-1][-1]
        
        rows = len(heights)
        cols = len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        graph = defaultdict(list)

        for row in range(rows):
            for col in range(cols):
                for d in directions:
                    new_row = row + d[0]
                    new_col = col + d[1]
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        val = abs(heights[row][col] - heights[new_row][new_col])
                        graph[(row, col)].append(((new_row, new_col), val))
        distances = dijkstra(graph, rows, cols)
        return distances