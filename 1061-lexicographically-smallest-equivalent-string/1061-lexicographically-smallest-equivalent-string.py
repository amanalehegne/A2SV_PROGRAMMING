class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str: 
        parent = dict()
        
        def find(node):
            if node not in parent:
                parent[node] = node
            elif node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 != parent2:
                if parent1 < parent2:
                    parent[parent2] = parent1
                else:
                    parent[parent1] = parent2
        
        sizeStr = len(s1)
        for i in range(sizeStr):
            union(s1[i], s2[i])
            
        res = []
        for char in baseStr:
            res.append(find(char))
        
        return "".join(res)
            
        