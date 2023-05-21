class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
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
        
        def groupItems():
            res = defaultdict(list)
            for node in parent:
                res[find(node)].append(node)
            
            return res
            
        users = dict()
        for account in accounts:
            accountSize = len(account)
            for i in range(1, accountSize):
                find(account[i])
                users[account[i]] = account[0]
                if i + 1 < accountSize:
                    union(account[i], account[i + 1])
        
        groups = groupItems()
        res = []
        for key in groups:
            res.append([users[key]] + sorted(groups[key]))
        
        return res
        

        
        
        
        
                
        
            