class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nodes = len(isConnected)
        rep = {i + 1 : i + 1 for i in range(nodes)}
        size = [1] * (nodes + 1)
        
        def find(rep, x):
            if x == rep[x]:
                return x

            rep[x] = find(rep, rep[x])
            return rep[x]
        
        def union(rep, size, x, y):
            x = find(rep, x)
            y = find(rep, y)
            if x == y:
                return
            sizeX = size[x]
            sizeY = size[y]
            if sizeX > sizeY:
                x, y = y, x

            rep[x] = y
            size[y] += size[x]
        
        for i in range(nodes):
            for j in range(nodes):
                if i != j and isConnected[i][j] == 1:
                    union(rep, size, i + 1, j + 1)
        
        for i in range(nodes):
            find(rep, i + 1)
        
        res = set()
        for key in rep:
            res.add(rep[key])
        
        return len(res)
                
                