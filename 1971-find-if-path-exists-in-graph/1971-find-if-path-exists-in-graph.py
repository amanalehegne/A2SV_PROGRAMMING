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
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            arr = adjList[node]
            seen.add(node)
            for nextNode in arr:
                if nextNode not in seen:
                    stack.append(nextNode)
                
        return False
            
            
        