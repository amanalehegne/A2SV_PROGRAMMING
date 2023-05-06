class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dic = defaultdict(list)
        self.dead = set()
        self.root = kingName
        

    def birth(self, parentName: str, childName: str) -> None:
        self.dic[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []
        stack = [self.root]
        while stack:
            current = stack.pop()
            children = self.dic[current]
            
            if current not in self.dead:
                res.append(current)
            
            size = len(children)
            for i in range(size):
                idx = size - 1 - i
                stack.append(children[idx])
                
        return res
                
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()