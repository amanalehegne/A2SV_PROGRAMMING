class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        edges = defaultdict(int)
        size = len(recipes)
        
        for i in range(size):
            arr = ingredients[i]
            for lst in arr:
                graph[lst].append(recipes[i])
                edges[recipes[i]] += 1
        
        
        def BFS(graph, queue, needed):
            res = []
            while queue:
                current = queue.pop()
                
                if current in needed:
                    res.append(current)
                
                neighbors = graph[current]
                for neighbor in neighbors:
                    edges[neighbor] -= 1
                    if edges[neighbor] == 0:
                        queue.append(neighbor)
            return res
        
        queue = deque(supplies)
        needed = set(recipes)
        
        return BFS(graph, queue, needed)
            