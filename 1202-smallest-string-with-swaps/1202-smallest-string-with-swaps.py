class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        strSize = len(s)
        rep = {i:i for i in range(strSize)}
        size = [0] * strSize
        
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
        
        for x, y in pairs:
            union(rep, size, x, y)
        
        def toChar(val):
            return chr(97 + val)
        
        dic = defaultdict(list)
        for i in range(strSize):
            parent = find(rep, i)
            dic[parent].append(i)
        
        for key in dic:
            dic[key] = sorted([s[i] for i in dic[key]], reverse=True)
        
        res = []
        for i in range(strSize):
            parent = find(rep, i)
            val = dic[parent].pop()
            res.append(val)
        
        return "".join(res)