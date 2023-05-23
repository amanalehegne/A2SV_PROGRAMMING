class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def DFS(graph, stack, seen):
            res = 0
            while stack:
                res += 1
                node = stack.pop()
                neighbours = graph[node]
                for neighbour in neighbours:
                    if neighbour not in seen:
                        stack.append(neighbour)
                        seen.add(neighbour)
            return res
        
        
        length = len(bombs)
        graph = defaultdict(list)
        for i in range(length):
            xi, yi, wi = bombs[i]
            for j in range(i + 1, length):
                xj, yj, wj = bombs[j]
                distance = (((xi - xj) ** 2) + ((yi - yj) ** 2)) ** 0.5
                if distance <= wi:
                    graph[i].append(j)
                if distance <= wj:
                    graph[j].append(i)
        
        res = 0
        for i in range(length):
            stack = [i]
            seen = set()
            seen.add(i)
            res = max(res, DFS(graph, stack, seen))
        
        return res
        
        
                