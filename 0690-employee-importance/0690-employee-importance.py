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
        

        def DFT(node, res, seen=set()):
            subordinates = dic[node][-1]
            res += dic[node][0]
            seen.add(node)
            for node in subordinates:
                if node not in seen:
                    res = DFT(node, res)
            return res
            
        
        
        return DFT(id, 0)
                    