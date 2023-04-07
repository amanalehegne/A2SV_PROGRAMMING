class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        [0,1],[1,2],[2,0]]
        0 - [1, 2]
        1 - [0, 2]
        2 - [1, 0]
        """
        adjList = defaultdict(list)
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        
        seen = set()
        
        def dfs(vertex):
            if vertex == destination:
                return True
            
            arr = adjList[vertex]
            seen.add(vertex)
            for nextVer in arr:
                if nextVer not in seen:
                    check = dfs(nextVer)
                    if check:
                        return True
            
            return False
    
        return dfs(source)
                
            
            
        