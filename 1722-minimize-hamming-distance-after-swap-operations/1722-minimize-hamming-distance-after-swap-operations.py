class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = dict()
        size = dict()
        
        def find(node):
            if node not in parent:
                parent[node] = node
                size[node] = 1
            elif node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            
            if size[parent1] < size[parent2]:
                parent1, parent2 = parent2, parent1
            
            parent[parent2] = parent1
            size[parent1] += size[parent2]
        
        def groupItems(item = parent):
            groups = defaultdict(list)
            for node in item:
                groups[find(node)].append(node)
            
            return groups
        
        for x, y in allowedSwaps:
            union(x, y)
        
        n = len(source)
        groups = groupItems([i for i in range(n)])
        res = 0
        for indices in groups.values():
            arr = defaultdict(int)
            
            for i in indices:
                arr[source[i]] += 1
                arr[target[i]] -= 1
            
            for val in arr.values():
                if val > 0: 
                    res += val
        
        return res
                