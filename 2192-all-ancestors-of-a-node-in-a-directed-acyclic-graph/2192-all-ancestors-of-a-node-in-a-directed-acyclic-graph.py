from collections import defaultdict, deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = [0 for _ in range(n)]
        graph = defaultdict(list)

        for form_, to_ in edges:
            indegree[to_] += 1
            graph[form_].append(to_)

        res = [set() for i in range(n)]

        def BFS(graph, indegree, queue, res):
            while queue:
                size = len(queue)
                current = queue.popleft()
                children = graph[current]
                for child in children:
                    indegree[child] -= 1
                    res[child].add(current)
                    res[child].update(res[current])
                    for ancestor in res[current]:
                        res[child].add(ancestor)

                    if indegree[child] == 0:
                        queue.append(child)

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                
        BFS(graph, indegree, queue, res)
            
        return [sorted(list(val)) for val in res]
