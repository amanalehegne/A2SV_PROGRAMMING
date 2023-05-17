class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for x, y in prerequisites:
            graph[x].append(y)
            indegree[y] += 1
        
        def BFS(graph, queue, res):
            while queue:
                node = queue.popleft()
                children = graph[node]
                for child in children:
                    indegree[child] -= 1
                    res[child].add(node)
                    res[child].update(res[node])
                    if indegree[child] == 0:
                        queue.append(child)
        
        res = defaultdict(set)
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        BFS(graph, queue, res)
        ans = []
        for x, y in queries:
            ans.append(x in res[y])
        
        return ans
        