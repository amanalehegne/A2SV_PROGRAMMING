class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        def DFS(root, path):
            path.append(root)
            
            if root + 1 == len(graph):
                res.append(path[:])
                return
                
            arr = graph[root]
             
            for node in arr:
                DFS(node, path)
                path.pop()
            
        DFS(0, [])
        return res