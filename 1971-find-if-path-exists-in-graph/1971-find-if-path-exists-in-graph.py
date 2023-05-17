class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rep = {i:i for i in range(n)}
        size = [1] * n
        
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
        
        def solution(rep, node1, node2):
            node1, node2 = find(rep, node1), find(rep, node2)
            return node1 == node2
        
        
        for x, y in edges:
            union(rep, size, x, y)

        return solution(rep, source, destination)
        
        
                