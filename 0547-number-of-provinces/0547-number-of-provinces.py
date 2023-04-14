class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        cols = len(isConnected[0])
        
        dic = defaultdict(list)
        
        for row in range(rows):
            for col in range(cols):
                if isConnected[row][col] and row != col:
                    dic[row + 1].append(col + 1)
        seen = set()
        def DFS(root):
            
            seen.add(root)
            arr = dic[root]
            for i in arr:
                if i not in seen:
                    DFS(i)
        
        size = len(isConnected) + 1
        res = 0
        for i in range(1, size):
            if i not in seen:
                DFS(i)
                res += 1 
        
        return res
                
        