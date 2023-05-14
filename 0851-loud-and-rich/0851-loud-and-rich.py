class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        def BFS(graph, indegree, queue, quiet, key):
            while queue:
                node = queue.popleft()
                children = graph[node]
                for child in children:
                    indegree[child] -= 1
                    
                    parentIdx = key[node] 
                    childIdx = key[child]
                    
                    if quiet[childIdx] > quiet[parentIdx]:
                        key[child] = parentIdx
                    
                    if indegree[child] == 0:
                        queue.append(child)
                        
        
        
        vertices = len(quiet)
        graph = defaultdict(list)
        indegree = [0] * vertices
        res = [i for i in range(vertices)]
        
        for start, end in richer:
            graph[start].append(end)
            indegree[end] += 1
        
        queue = deque()
        for node in range(vertices):
            if indegree[node] == 0:
                queue.append(node)
        
        
        BFS(graph, indegree, queue, quiet, res)
        return res
        