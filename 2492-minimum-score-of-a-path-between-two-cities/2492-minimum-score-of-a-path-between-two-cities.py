class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = {i + 1:i + 1 for i in range(n)}
        size = [1] * (n + 1)
        res = [float("inf")] * (n + 1)
        
        def find(rep, node):
            if node == rep[node]:
                return node
            rep[node] = find(rep, rep[node])
            return rep[node]
        
        def union(rep, size, node1, node2, weight):
            node1 = find(rep, node1)
            node2 = find(rep, node2)
            if node1 == node2:
                res[node1] = min(res[node1], weight)
                return
            size1, size2 = size[node1], size[node2]
            if size1 > size2:
                node1, node2 = node2, node1
            
            rep[node1] = node2
            size[node2] += size[node1]
            res[node2] = min(res[node2], weight, res[node1])
            
            
        
        def solution(rep, node1, node2):
            node1, node2 = find(rep, node1), find(rep, node2)
            return node1 == node2
        
        for node1, node2, weight in roads:
            union(rep, size, node1, node2, weight)

        return res[find(rep, n)]
        
            