class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def DFS(graph, color, stack):
            while stack:
                node = stack.pop()
                if color[node] == -1:
                    color[node] = 0
                for child in graph[node]:
                    if color[child] == -1:
                        stack.append(child)
                        color[child] = 1 - color[node]
                    elif color[child] == color[node]:
                        return False
            return True

        graph = defaultdict(list)
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        
        stack = []
        color = [-1] * (n + 1)
        
        for i in range(n):
            val = i + 1
            stack.append(val)
        
        return DFS(graph, color, stack)
                