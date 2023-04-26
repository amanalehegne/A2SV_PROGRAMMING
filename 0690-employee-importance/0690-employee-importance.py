"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = defaultdict(list)
        for employee in employees:
            dic[employee.id].append(employee.importance)
            dic[employee.id].append(employee.subordinates)
        
        res = [0]
        def DFT(node, seen=set()):
            subordinates = dic[node][-1]
            res[0] += dic[node][0]
            seen.add(node)
            for node in subordinates:
                if node not in seen:
                    DFT(node)
        
        DFT(id)
        return res[0]
                    