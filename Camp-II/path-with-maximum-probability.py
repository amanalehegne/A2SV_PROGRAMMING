class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        def dijkstra(graph, start, end):
            probabilities = {node: float('-inf') for node in range(n)}
            probabilities[start] = 1
            visited = set()

            priority_queue = [(-1, start)]

            while priority_queue:
                current_probability, current_node = heapq.heappop(priority_queue)
                current_probability = -current_probability
                if current_node == end:
                    return probabilities[end]
                if current_node in visited:
                    continue
                visited.add(current_node)

                for neighbor, weight in graph[current_node]:

                    probability = current_probability * weight
                    if probability > probabilities[neighbor]:
                        probabilities[neighbor] = probability

                    heapq.heappush(priority_queue, (-probability, neighbor))
            
            return 0
        
        graph = defaultdict(list)
        size = len(edges)
        for i in range(size):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        return dijkstra(graph, start_node, end_node)