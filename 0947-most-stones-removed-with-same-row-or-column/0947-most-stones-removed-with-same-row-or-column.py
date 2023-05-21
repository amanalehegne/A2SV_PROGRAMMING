class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
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
            
            if parent1 != parent2:
                if size[parent1] < size[parent2]:
                    parent1, parent2 = parent2, parent1

                parent[parent2] = parent1
                size[parent1] += size[parent2]
        
        grouping = defaultdict(list)
        for row, col in stones:
            grouping[(row, "Row")].append((row, col))
            grouping[(col, "Col")].append((row, col))
        
        for key in grouping:
            length = len(grouping[key])
            for i in range(length - 1):
                union(grouping[key][i], grouping[key][i + 1])
        
        count = set()
        for point in stones:
            point = tuple(point)
            count.add(find(point))
        
        return len(stones) - len(count)