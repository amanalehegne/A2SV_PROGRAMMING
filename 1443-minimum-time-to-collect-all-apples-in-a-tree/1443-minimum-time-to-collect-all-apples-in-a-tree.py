class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        hasPath = [False for i in range(n)]
        
        seen = set()
        seen.add(0)
        
        def findPath(root, path):
            children = dic[root]
            for child in children:
                if child not in seen:
                    seen.add(child)
                    path.append(child)
                    if hasApple[child]:
                        for val in path:
                            hasPath[val] = True
                    findPath(child, path)
                    path.pop()
        
        def solution(root):
            seen = set()
            stack = [root]
            seen.add(root)
            res = 0
            
            while stack:
                node = stack.pop()
                children = dic[node]                
                size = len(children)
                
                for i in range(size):
                    idx = size - i - 1
                    if (children[idx] not in seen) and (hasApple[children[idx]] or hasPath[children[idx]]):
                        seen.add(children[idx])
                        stack.append(children[idx])
                        res += 1
            return res

        
        dic = defaultdict(list)
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)
        
        findPath(0, [0])
        
        return solution(0) * 2
        