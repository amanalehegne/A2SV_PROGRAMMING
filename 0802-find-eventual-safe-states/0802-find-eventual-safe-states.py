class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def DFS(graph, node, color, res):
            if color[node] == 0:
                color[node] = 1
                children = graph[node]
                for child in children:
                    if color[child] == 0:
                        val = DFS(graph, child, color, res)
                        if not val:
                            return val
                    elif color[child] == 1:
                        return False

                color[node] = 2
                res.append(node)
                return True
        
        size = len(graph)
        color = [0] * size
        res = []
        for node in range(size):
            DFS(graph, node, color, res)
        
        return sorted(res)