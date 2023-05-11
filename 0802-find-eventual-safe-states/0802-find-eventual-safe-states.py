class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node, color, graph):
            color[node] = 1 # Current Path
            for child in graph[node]:
                if color[child] == 1 or (color[child] == 0 and not dfs(child, color, graph)):
                    return False

            color[node] = 2 # Visited
            return True

        color = [0] * len(graph)
        res = []
        for i in range(len(graph)):
            if dfs(i, color, graph):
                res.append(i)

        return res