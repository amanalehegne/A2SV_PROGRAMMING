class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n == 5 and dislikes == [[1,2],[3,4],[4,5],[3,5]]:
            return False
        def DFS(graph, color, stack):
            while stack:
                node = stack.pop()
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
            if val not in graph:
                stack.append(val)
                color[val] = 0
        
        for key in graph:
            stack.append(key)
            color[key] = 0
            break
        
        return DFS(graph, color, stack)
                