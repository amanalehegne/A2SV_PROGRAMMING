class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        size = len(adjacentPairs) + 1
        
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
        
        
        offset = 0
        queue = deque()
        for key in indegree:
            if indegree[key] == 1:
                queue.append((key, offset))
                offset += 1
        
        def BFS(graph, indegree, size, queue):
            res = [0] * size
            left, right = 0, size - 1
            while size > 0:
                level = len(queue)
                size -= level
                for _ in range(level):
                    node, offset = queue.popleft()
                    
                    if offset == 0:
                        res[left] = node
                        left += 1
                    else:
                        res[right] = node
                        right -= 1
                        
                    children = graph[node]
                    for child in children:
                        indegree[child] -= 1
                        if indegree[child] == 1:
                            queue.append((child, offset))
            return res
        
        return BFS(graph, indegree, size, queue)
                            
                            
            