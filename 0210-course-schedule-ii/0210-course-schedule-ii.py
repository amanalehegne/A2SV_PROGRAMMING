class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        edges = defaultdict(int)
        for x, y in prerequisites:
            dic[y].append(x)
            edges[x] += 1
        
        
        def BFS(dic, queue):
            res = []
            while queue:
                current = queue.popleft()
                res.append(current)
                
                children = dic[current]
                for child in children:
                    edges[child] -= 1
                    if edges[child] == 0:
                        queue.append(child)
            return res
        
        queue = deque()
        for i in range(numCourses):
            if edges[i] == 0:
                queue.append(i)
        
        val = BFS(dic, queue)
        if len(val) != numCourses:
            val = []
        
        return val
        
        
        

                