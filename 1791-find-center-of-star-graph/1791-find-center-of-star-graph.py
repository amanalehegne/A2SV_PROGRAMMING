class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        n = len(graph) - 1
        for key in graph:
            if len(graph[key]) == n:
                return key
    