class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rep = {i + 1:i + 1 for i in range(n)}
        size = [1] * (n + 1)
        
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
        
        def checkLoop(rep, node1, node2):
            node1, node2 = find(rep, node1), find(rep, node2)
            return node1 == node2
        
        for x, y in edges:
            if checkLoop(rep, x, y):
                return [x, y]
            union(rep, size, x, y)
            