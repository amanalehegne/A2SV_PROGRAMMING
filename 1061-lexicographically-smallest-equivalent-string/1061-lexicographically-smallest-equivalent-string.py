class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str: 
        # Get the alphabets from a to z
        rep = {chr(i) : chr(i) for i in range(97, 123)}

        
        def find(rep, node):
            if node == rep[node]:
                return node
            rep[node] = find(rep, rep[node])
            return rep[node]
        
        def union(rep, node1, node2):
            node1 = find(rep, node1)
            node2 = find(rep, node2)
            
            # We choose the lexographically smallest parent to represent the union of the two groups
            val = min(node1, node2)
            if node1 != node2:
                rep[node1] = val
                rep[node2] = val
        
        sizeStr = len(s1)
        for i in range(sizeStr):
            node1 = s1[i]
            node2 = s2[i]
            union(rep, node1, node2)
        
        ans = []
        for char in baseStr:
            # Get the parent (which is the smallest lexographically) of the current character
            ans.append(find(rep, char))
        
        return "".join(ans)
        