class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = 26
        rep = {chr(i) : chr(i) for i in range(97, 123)}
        size = [1] * (n + 1)
        
        def find(rep, node):
            if node == rep[node]:
                return node
            rep[node] = find(rep, rep[node])
            return rep[node]
        
        def getSize(size, node):
            return size[ord(node) - ord('a')]
        
        def union(rep, size, node1, node2):
            node1 = find(rep, node1)
            node2 = find(rep, node2)
            
            if node1 == node2:
                return
            size1, size2 = getSize(size, node1), getSize(size, node2)
            if size1 > size2:
                node1, node2 = node2, node1
            
            rep[node1] = node2
            size[ord(node2) - ord('a')] += getSize(size, node1)
        
        def solution(rep, node1, node2):
            return find(rep, node1) == find(rep, node2)
        
        for eqn in equations:
            char1, char2 = eqn[0], eqn[3]
            sign = eqn[1]
            if sign == "=":
                union(rep, size, char1, char2)

                
        for eqn in equations:
            char1, char2 = eqn[0], eqn[3]
            sign = eqn[1]
            if sign == "!":
                if solution(rep, char1, char2):
                    return False
                

                
        
        return True